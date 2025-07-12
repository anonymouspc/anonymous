export module anonymous:basic.concepts:operators;
import        std;

export namespace anonymous
{
    template < class type >               concept plusable        = requires { std::declval<type >() +   std::declval<type >(); };
    template < class type1, class type2 > concept plusable_to     = requires { std::declval<type1>() +   std::declval<type2>(); };
    template < class type1, class type2 > using   plus_result     = decltype ( std::declval<type1>() +   std::declval<type2>()  );
    template < class type >               concept minusable       = requires { std::declval<type >() -   std::declval<type >(); };
    template < class type1, class type2 > concept minusable_to    = requires { std::declval<type1>() -   std::declval<type2>(); };
    template < class type1, class type2 > using   minus_result    = decltype ( std::declval<type1>() -   std::declval<type2>()  );
    template < class type >               concept multipliable    = requires { std::declval<type >() *   std::declval<type >(); };
    template < class type1, class type2 > concept multipliable_to = requires { std::declval<type1>() *   std::declval<type2>(); };
    template < class type1, class type2 > using   multiply_result = decltype ( std::declval<type1>() *   std::declval<type2>()  );
    template < class type >               concept dividable       = requires { std::declval<type >() /   std::declval<type >(); };
    template < class type1, class type2 > concept dividable_to    = requires { std::declval<type1>() /   std::declval<type2>(); };
    template < class type1, class type2 > using   divide_result   = decltype ( std::declval<type1>() /   std::declval<type2>()  );
    template < class type >               concept modulable       = requires { std::declval<type >() %   std::declval<type >(); };
    template < class type1, class type2 > concept modulable_to    = requires { std::declval<type1>() %   std::declval<type2>(); };
    template < class type1, class type2 > using   modulus_result  = decltype ( std::declval<type1>() %   std::declval<type2>()  );
    template < class type >               concept equalable       = requires { std::declval<type >() ==  std::declval<type >(); };
    template < class type1, class type2 > concept equalable_to    = requires { std::declval<type1>() ==  std::declval<type2>(); };
    template < class type >               concept comparable      = requires { std::declval<type >() <=> std::declval<type >(); };
    template < class type1, class type2 > concept comparable_to   = requires { std::declval<type1>() <=> std::declval<type2>(); };
    template < class type1, class type2 > using   compare_result  = decltype ( std::declval<type1>() <=> std::declval<type2>()  );
}