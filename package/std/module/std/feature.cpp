module;
#include <version>

export module std:feature;
// #ifndef __cpp_lib_linalg
// export import    :feature.linalg;
// #endif
// #if not defined(__cpp_lib_mdspan) and not defined(__clang__)
// export import    :feature.mdspan;
// #endif
// export import    :feature.ranges;
#ifndef __cpp_lib_sender
export import    :feature.sender;
#endif
#ifndef __cpp_lib_stacktrace
export import    :feature.stacktrace;
#endif
