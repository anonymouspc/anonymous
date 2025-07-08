module;
#ifdef __clang__
    #pragma clang diagnostic ignored "-Wreserved-module-identifier"
#endif
#include <version>

export module std.feature:ranges;

#ifndef __cpp_lib_ranges_as_const
    export import :ranges.as_const;
#endif

#ifndef __cpp_lib_ranges_chunk
    export import :ranges.chunk;
#endif

#ifndef __cpp_lib_ranges_join_with
    export import :ranges.join_with;
#endif

#ifndef __cpp_lib_ranges_starts_ends_with
    export import :ranges.starts_ends_with;
#endif

#ifndef __cpp_lib_ranges_stride
    export import :ranges.stride;
#endif

#ifndef __cpp_lib_ranges_zip
    export import :ranges.zip;
#endif