export module anonymous:basic.algorithm.loop;
import                 :basic.algorithm.range;
import        std;

export namespace anonymous
{
    template < int min, int max, int stride = 1 > constexpr void for_constexpr     ( auto&& );
    template < int min, int max, int stride = 1 > constexpr bool all_of_constexpr  ( auto&& );
    template < int min, int max, int stride = 1 > constexpr bool any_of_constexpr  ( auto&& );
    template < int min, int max, int stride = 1 > constexpr bool none_of_constexpr ( auto&& );



    template < int min, int max, int stride >
    constexpr void for_constexpr ( auto&& ops )
    {
        if constexpr ( ( stride > 0 and min <= max ) or
                       ( stride < 0 and min >= max ) )
            ops.template operator()<min>();

        if constexpr ( ( stride > 0 and min <= max - stride ) or 
                       ( stride < 0 and min >= max - stride ) )
            for_constexpr<min+stride,max,stride>(std::forward<decltype(ops)>(ops));
    }

    template < int min, int max, int stride >
    constexpr bool all_of_constexpr ( auto&& preds )
    {
        bool result = true;
        for_constexpr<min,max,stride>([&] <int index> { result = result and preds.template operator()<index>(); });
        return result;
    }

    template < int min, int max, int stride >
    constexpr bool any_of_constexpr ( auto&& preds )
    {
        bool result = false;
        for_constexpr<min,max,stride>([&] <int index> { result = result or preds.template operator()<index>(); });
        return result;
    }

    template < int min, int max, int stride >
    constexpr bool none_of_constexpr ( auto&& preds )
    {
        bool result = true;
        for_constexpr<min,max,stride>([&] <int index> { result = result and not preds.template operator()<index>(); });
        return result;
    }
}