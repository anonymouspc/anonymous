1. 
  - 当前的：Package(A)需要Module(A.X)依赖于Module(B.M)依赖于Package(B)需要Module(B.N)
  - 而UnitDependencyLogger的：Package(A)需要Module(A.X)依赖于Module(B.M)，因为并未返到package得不到Module(B.N)
  - 考虑：加入@dependency，后者自动分析依赖关系，出现循环时报错，出现无害循环时打破循环。当前这个二次探查确实混乱。

2. 

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