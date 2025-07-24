module;
#ifdef __clang__
    #pragma clang diagnostic ignored "-Wreserved-module-identifier"
#endif
#include <version>

export module std:feature.ranges;
#ifndef __cpp_lib_ranges_as_const
export import    :feature.ranges.as_const;
#endif
#ifndef __cpp_lib_ranges_chunk
export import    :feature.ranges.chunk;
#endif
#ifndef __cpp_lib_ranges_join_with
export import    :feature.ranges.join_with;
#endif
#ifndef __cpp_lib_ranges_starts_ends_with
export import    :feature.ranges.starts_ends_with;
#endif
#ifndef __cpp_lib_ranges_stride
export import    :feature.ranges.stride;
#endif
#if not defined(__cpp_lib_ranges_zip) and not defined(__clang__)
export import    :feature.ranges.zip;
#endif