export module std:compiler;

#if defined(__GNUC__) and not defined(__clang__)
export import    :compiler.gcc;
#elifdef __clang__
export import    :compiler.clang;
#elif defined(_MSC_VER) and not defined(__clang__)
export import    :compiler.msvc;
#endif