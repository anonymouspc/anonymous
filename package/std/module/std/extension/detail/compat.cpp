module;
#include <stdio.h>

module std:extension.detail.compat;
import    :compiler;

template < class type > 
concept assert_printable = requires (type str)
    {
        { str.size() } -> std::convertible_to<std::size_t>;
        { str.data() } -> std::convertible_to<const char*>;
    };


auto stdin_  = stdin;
auto stdout_ = stdout;
auto stderr_ = stderr;
