3. 对编译错误的parse，写在Compiler类里面。

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