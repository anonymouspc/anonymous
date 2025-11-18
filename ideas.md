1. 
  - 错误的
    - 假设Module[A, B, C], Package[P, Q, R] st. A->P, P->A, P->B, B->Q, Q->B, Q->C, C->R,
    - 那么A未直接导入C，即A不需要C就能build.

2. 两种思路：
  1. 在unit_imports_logger中直接给出package.import_packages, dependency_cycle.
    - 优点：参数和返回值都是class Package/Module, 而非name，对称
    - unit_imports_logger表示**臣妾做不到**，太臃肿，其他logger都很轻松
    - 在unit_imports_logger内
      - 方法一
        - 假设有Module节点A, B
        - B被外部发起
        - B->C (C.stack='B')
        - A被外部发起
        - A->B (B waiting...)
        - C->A (A waiting...)
        - C ok! B ok! A ok!
        - 未检测到循环依赖，**否决**
      - 方法二
        - 每个节点计算完后，等待所有出边计算完，沿所有出边递归走一遍，仅检查到不到自身
        - 设置标志，自己检查过了
  2. 在unique里夹带私货，使得A->P, P->A需要等待A.await import_modules, 无需等待A.await import_package。
    - 假如B并行执行构造函数，B.await import_modules时P->B应该等待
    - 假如B未被要求，纯粹由P->B，那么B只会执行到它需要的部分，import_package永远不会初始化，没人await它
    - 假如P->B, B->C, P->C => C->P，如果C先由B->C调起，那么C的import_package也应该不被await，否则P->B->C->P循环死锁
    - 即module await import_modules也要在unique夹带私货
    - **否决**


3. Module._file_to_name是不准确的
 - file是**必要的**，因为
   - ModuleImportsLogger需要查询一个Package旗下所有Module from file
     - Package(boost)仅查询Module(boost)
   - 用户需要file in iterator dir
   - file_to_name可以是async的
   - 考虑重命名code_file为file
 - 可以Module.__ainit__(self, name, file)，然后decorator指定只需要提供一个就可以了。
 - Package.exist()看看有无必要。
 - !! Package只要查找自己的modules直接的import modules的package即可，不用递归查找
 
 - import_packages, module_dir, source_dir等写在cppmake.py里

4. unit syncable -> registerable, __init__(fileable)

5. 
```cpp
module;
#include <tuple>

export module ideas;

export 
class my_type { };

namespace std 
{
    template < >
    class tuple_size<my_type>
    {
        public:
            constexpr static const int value = 2;
    };
}
```
目前可以导出特化，找找看哪些不能导出。