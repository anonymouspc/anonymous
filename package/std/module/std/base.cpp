export module std:base;

#ifdef _GLIBCXX_RELEASE
export import    :base.libstdcxx;
#elifdef _LIBCPP_VERSION
export import    :base.libcxx;
#else
#error "not coded yet"
#endif