module;
#include <cassert> // macro: aassert.
#include <csignal> // macros: SIGINT, SIGABRT, ...
#include <ranges> // utilities for ranges.

export module anonymous:basic;

import std;
import stdexec;
import plf;
import boost;
import Eigen;
import tbb;
import cuda;
import thrust;

export namespace std
{
    // Std.feature
    #ifndef __cpp_lib_aligned_accessor
        #include "std/aligned_accessor.hpp"
    #endif

    #ifndef __cpp_lib_inplace_vector
        #include "std/inplace_vector.hpp"
    #endif

    #ifndef __cpp_lib_is_layout_compatible
        #include "std/is_layout_compatible.hpp"
    #endif

    #ifndef __cpp_lib_mdspan
        #include "std/mdspan.hpp"
    #endif

    #ifndef __cpp_lib_ranges_as_const
        #include "std/ranges/const_iterator.hpp"
    #endif

    #ifndef __cpp_lib_ranges_chunk
        #include "std/ranges/chunk_view.hpp"
    #endif

    #ifndef __cpp_lib_ranges_join_with
        #include "std/ranges/join_with_view.hpp"
    #endif 

    #ifndef __cpp_lib_ranges_starts_ends_with
        #include "std/ranges/starts_ends_with.hpp"
    #endif

    #ifndef __cpp_lib_ranges_stride
        #include "std/ranges/stride_view.hpp"
    #endif

    #ifndef __cpp_lib_ranges_zip
        #include "std/ranges/zip_view.hpp"
    #endif

    #ifndef __cpp_lib_stacktrace
        #include "std/stacktrace.hpp"
    #endif

    #ifndef __cpp_lib_submdspan
        #include "std/submdspan.hpp"
    #endif

    #ifndef __cpp_lib_text_encoding
        #include "std/text_encoding.hpp"
    #endif

    // Std.extension
    #include "std/format_type_info.hpp"
}

export namespace std
{
    using namespace plf; // C++26 proposal.
}

export namespace std::execution
{
    using namespace stdexec; // C++26 proposal.
}

export namespace anonymous
{
    /// Config
    #ifdef NDEBUG
        constexpr bool debug = false;
    #else
        constexpr bool debug = true;
    #endif

    /// Algorithm

                                                  constexpr decltype(auto) first_value_of    ( auto&&... );
                                                  constexpr decltype(auto) last_value_of     ( auto&&... );
    template < int index >                        constexpr decltype(auto) index_value_of    ( auto&&... );
    template < int min, int max, int stride = 1 > constexpr void           for_constexpr     ( auto&& );
    template < int min, int max, int stride = 1 > constexpr bool           all_of_constexpr  ( auto&& );
    template < int min, int max, int stride = 1 > constexpr bool           any_of_constexpr  ( auto&& );
    template < int min, int max, int stride = 1 > constexpr bool           none_of_constexpr ( auto&& );

    /// Device
    class cpu;
    class cuda;
    class system;
    class tbb;

    /// Exception
    class exception;
        class logic_error;
            class value_error;
                class index_error;
                class key_error;
            class type_error;
        class runtime_error;
            class text_error;
                class encode_error;
                class format_error;
                class parse_error;
                class regex_error;
            class io_error;
                class file_error;
                class pipe_error;
                class serial_port_error;
                class network_error;
            class device_error;
                class cuda_error;
                class opencl_error;
                class tbb_error;
            class math_error;
                class linalg_error;

    /// Range
    constexpr random_access_range auto range ( integral auto );
    constexpr random_access_range auto range ( integral auto, integral auto );
    constexpr random_access_range auto range ( integral auto, integral auto, integral auto );

    /// Include
    #include "utility/internal/macro.cpp"
    #include "algorithm/algorithm.hpp"
    #include "number/number.hpp"
    #include "range/range.hpp"
    #include "exception/exception.hpp"
    #include "device/device.hpp"

    /// Global
                 cpu::execution_context_type& execution_context = cpu::execution_context;
    thread_local cpu::random_context_type&    random_context    = cpu::random_context;
}

export namespace std
{
    #include "utility/external/std/std.hpp"
}



