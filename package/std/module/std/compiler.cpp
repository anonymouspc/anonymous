export module std:compiler;
#ifdef _GLIBCXX_RELEASE
export import    :compiler.libstdcxx;
#elifdef _LIBCPP_VERSION
export import    :compiler.libcxx;
#else
#error "not coded yet"
#endif