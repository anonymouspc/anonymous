module;
#ifdef __clang__
    #pragma clang diagnostic ignored "-Wreserved-module-identifier"
#endif
#include <version>

export module std.feature:aligned_accessor;
#ifndef __cpp_lib_mdspan
    import :mdspan;
#endif
import        std.compiler;

export namespace std
{
    template < class type, size_t align >
    using aligned_accessor = default_accessor<type>;
}
