module;
#ifdef __clang__
    #pragma clang diagnostic ignored "-Wreserved-module-identifier"
#endif

export module std:feature.is_layout_compatible;

export namespace std
{
    template < class type1, class type2 >
    struct is_layout_compatible
    {
        static constexpr const bool value = (sizeof(type1) == sizeof(type2));
    };
}

