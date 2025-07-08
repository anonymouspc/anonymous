module;
#ifdef __clang__
    #pragma clang diagnostic ignored "-Wreserved-module-identifier"
#endif

export module std.compiler;

#if defined(__GNUC__) and not defined(__clang__)
    export import :gcc;
#elifdef __clang__
    export import :clang;
#elif defined(_MSC_VER) and not defined(__clang__)
    export import :msvc;
#endif