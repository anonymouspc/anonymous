export module anonymous.basic.config;

export namespace anonymous
{
    #ifndef NDEBUG
        constexpr bool debug = true;
    #else
        constexpr bool debug = false;
    #endif
}
