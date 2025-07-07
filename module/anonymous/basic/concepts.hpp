export module anonymous.basic.concepts;
import std;

export namespace anonymous
{
    /// Concept



    template < class type >                                    using          iterator_value_type                = std::iter_value_t                      <type>;
    template < class type >                                    using          iterator_reference                 = std::iter_reference_t                  <type>;
    template < class type >                                    using          iterator_pointer                   = std::iterator_traits                   <type>::pointer;
    template < class type >                                    using          iterator_difference_type           = std::iter_difference_t                 <type>;
    template < class type >                                    using          range_value_type                   = std::ranges::range_value_t             <type>;
    template < class type >                                    using          range_reference                    = std::ranges::range_reference_t         <type>;
    template < class type >                                    using          range_difference_type              = std::ranges::range_difference_t        <type>;                       
    template < class type >                                    using          range_iterator                     = std::ranges::iterator_t                <type>; 
    template < class type >                                    using          range_const_iterator               = std::ranges::const_iterator_t          <type>;
    template < class type >                                    using          range_sentinel                     = std::ranges::sentinel_t                <type>; 
    template < class type >                                    using          range_const_sentinel               = std::ranges::const_sentinel_t          <type>;

    template < class type >                                    constexpr int  tuple_size                         = std::tuple_size<type>::value;
    template < int index, class type >                         using          tuple_element                      = std::tuple_element<(index>=0) ? size_t(index-1) : size_t(index+int(std::tuple_size<type>::value)),type>::type;



    template < class type >                                    concept        integral                           = std::signed_integral<type>;
    template < class type >                                    concept        floating_point                     = std::floating_point <type>;
    template < class type >                                    concept        numeric                            = std::signed_integral<type> or std::floating_point<type>;

    template < class type >                                    concept        input_iterator                     = std::input_iterator                    <type>;
    template < class type >                                    concept        forward_iterator                   = std::forward_iterator                  <type>;
    template < class type >                                    concept        bidirectional_iterator             = std::bidirectional_iterator            <type>;
    template < class type >                                    concept        random_access_iterator             = std::random_access_iterator            <type>;
    template < class type >                                    concept        contiguous_iterator                = std::contiguous_iterator               <type>;
    template < class type >                                    concept        input_range                        = std::ranges::input_range               <type>;
    template < class type >                                    concept        forward_range                      = std::ranges::forward_range             <type>;
    template < class type >                                    concept        bidirectional_range                = std::ranges::bidirectional_range       <type>;
    template < class type >                                    concept        random_access_range                = std::ranges::random_access_range       <type>;
    template < class type >                                    concept        contiguous_range                   = std::ranges::contiguous_range          <type>;

    template < class type1, class type2 >                      concept        same_as                            = std::same_as                           <type1,type2>;
    template < class type1, class type2 >                      concept        base_of                            = std::derived_from                      <type2,type1>        and ( not std::same_as<type1,type2> ); // std::is_base_of allows private/protected extends, while std::derived_from does not.
    template < class type1, class type2 >                      concept        derived_from                       = std::derived_from                      <type1,type2>        and ( not std::same_as<type1,type2> ); // std::derived_from<type,type> (where type is class or union) is true.
    template < class type1, class type2 >                      concept        constructible_to                   = std::constructible_from                <type2,type1>;
    template < class type1, class type2 >                      concept        nothrow_constructible_to           = std::is_nothrow_constructible          <type2,type1>::value;
    template < class type1, class type2 >                      concept        convertible_to                     = std::convertible_to                    <type1,type2>        and constructible_to        <type1,type2>; // Make convertible >= constructible.
    template < class type1, class type2 >                      concept        nothrow_convertible_to             = std::is_nothrow_convertible            <type1,type2>::value and nothrow_constructible_to<type1,type2>; // Make convertible >= constructible.
    template < class type1, class type2 >                      concept        assignable_from                    = std::assignable_from                   <type1,type2>;
    template < class type1, class type2 >                      concept        nothrow_assignable_from            = std::is_nothrow_assignable             <type1,type2>::value;
    template < class type1, class type2 >                      concept        swappable_with                     = std::swappable_with                    <type1,type2>;
    template < class type1, class type2 >                      concept        nothrow_swappable_with             = std::is_nothrow_swappable_with         <type1,type2>::value;
    template < class type1, class type2 >                      concept        common_with                        = std::common_with                       <type1,type2>;
    template < class type1, class type2 >                      concept        common_reference_with              = std::common_reference_with             <type1,type2>;
    template < class type1, class type2 >                      concept        layout_compatible_with             = std::is_layout_compatible              <type1,type2>::value;  

    template < class type >                                    concept        plusable                           = requires { std::declval<type >() +   std::declval<type >(); };
    template < class type1, class type2 >                      concept        plusable_to                        = requires { std::declval<type1>() +   std::declval<type2>(); };
    template < class type1, class type2 >                      using          plus_result                        = decltype ( std::declval<type1>() +   std::declval<type2>()  );
    template < class type >                                    concept        minusable                          = requires { std::declval<type >() -   std::declval<type >(); };
    template < class type1, class type2 >                      concept        minusable_to                       = requires { std::declval<type1>() -   std::declval<type2>(); };
    template < class type1, class type2 >                      using          minus_result                       = decltype ( std::declval<type1>() -   std::declval<type2>()  );
    template < class type >                                    concept        multipliable                       = requires { std::declval<type >() *   std::declval<type >(); };
    template < class type1, class type2 >                      concept        multipliable_to                    = requires { std::declval<type1>() *   std::declval<type2>(); };
    template < class type1, class type2 >                      using          multiply_result                    = decltype ( std::declval<type1>() *   std::declval<type2>()  );
    template < class type >                                    concept        dividable                          = requires { std::declval<type >() /   std::declval<type >(); };
    template < class type1, class type2 >                      concept        dividable_to                       = requires { std::declval<type1>() /   std::declval<type2>(); };
    template < class type1, class type2 >                      using          divide_result                      = decltype ( std::declval<type1>() /   std::declval<type2>()  );
    template < class type >                                    concept        modulable                          = requires { std::declval<type >() %   std::declval<type >(); };
    template < class type1, class type2 >                      concept        modulable_to                       = requires { std::declval<type1>() %   std::declval<type2>(); };
    template < class type1, class type2 >                      using          modulus_result                     = decltype ( std::declval<type1>() %   std::declval<type2>()  );
    template < class type >                                    concept        equalable                          = requires { std::declval<type >() ==  std::declval<type >(); };
    template < class type1, class type2 >                      concept        equalable_to                       = requires { std::declval<type1>() ==  std::declval<type2>(); };
    template < class type >                                    concept        comparable                         = requires { std::declval<type >() <=> std::declval<type >(); };
    template < class type1, class type2 >                      concept        comparable_to                      = requires { std::declval<type1>() <=> std::declval<type2>(); };
    template < class type1, class type2 >                      using          compare_result                     = decltype ( std::declval<type1>() <=> std::declval<type2>()  );

}
