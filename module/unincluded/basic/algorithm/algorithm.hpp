template < int min, int max, int stride = 1 > constexpr void           for_constexpr     ( auto&& );
template < int min, int max, int stride = 1 > constexpr bool           all_of_constexpr  ( auto&& );
template < int min, int max, int stride = 1 > constexpr bool           any_of_constexpr  ( auto&& );
template < int min, int max, int stride = 1 > constexpr bool           none_of_constexpr ( auto&& );

#include "algorithm.cpp"