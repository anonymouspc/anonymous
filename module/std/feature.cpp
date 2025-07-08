module;
#ifdef __clang__
    #pragma clang diagnostic ignored "-Wreserved-module-identifier"
#endif
#include <version>

export module std.feature;

#ifndef __cpp_lib_aligned_accessor
    export import :aligned_accessor;
#endif

#ifndef __cpp_lib_hive
    export import :hive;
#endif

#ifndef __cpp_lib_inplace_vector
    export import :inplace_vector;
#endif

#ifndef __cpp_lib_is_layout_compatible
    export import :is_layout_compatible;
#endif

#ifndef __cpp_lib_linalg
    export import :linalg;
#endif

#ifndef __cpp_lib_mdspan
    export import :mdspan;
#endif

export import :ranges;

#ifndef __cpp_lib_sender
    export import :sender;
#endif

#ifndef __cpp_lib_stacktrace
    export import :stacktrace;
#endif

#ifndef __cpp_lib_submdpsan
    export import :submdspan;
#endif

#ifndef __cpp_lib_text_encoding
    export import :text_encoding;
#endif
