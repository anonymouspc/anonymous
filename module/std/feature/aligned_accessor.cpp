module;
#include <version>

export module std:feature.aligned_accessor;
import           :compiler;
#ifndef __cpp_lib_mdspan
import           :feature.mdspan;
#endif

export namespace std::inline feature
{
    template < class type, size_t align >
    using aligned_accessor = default_accessor<type>;
}
