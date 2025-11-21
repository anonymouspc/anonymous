export module std:compiler.libcxx;
#if _LIBCXX_VERSION < 20000
#error "libcxx version too low"
#elif _LIBCXX_VERSION >= 21000 and _LIBCXX_VERSION < 22000
export import    :compiler.libcxx.v21;
#elif _LIBCXX_VERSION >= 22000 and _LIBCXX_VERSION < 23000
export import    :compiler.libcxx.v22;
#else
#error "libcxx version too high"
#endif