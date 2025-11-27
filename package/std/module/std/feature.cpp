module;
#include <version>

export module std:feature;
#if not defined(__cpp_lib_aligned_accessor) and not defined(__clang__)
export import    :feature.aligned_accessor;
#endif
#ifndef __cpp_lib_hive
export import    :feature.hive;
#endif
#ifndef __cpp_lib_inplace_vector
export import    :feature.inplace_vector;
#endif
#ifndef __cpp_lib_is_layout_compatible
export import    :feature.is_layout_compatible;
#endif
// #ifndef __cpp_lib_linalg
// export import    :feature.linalg;
// #endif
#if not defined(__cpp_lib_mdspan) and not defined(__clang__)
export import    :feature.mdspan;
#endif
// export import    :feature.ranges;
#ifndef __cpp_lib_sender
export import    :feature.sender;
#endif
#ifndef __cpp_lib_stacktrace
export import    :feature.stacktrace;
#endif
#ifndef __cpp_lib_submdpsan
export import    :feature.submdspan;
#endif
#ifndef __cpp_lib_text_encoding
export import    :feature.text_encoding;
#endif
