export module anonymous:basic.concepts:core;
import        std;

export namespace anonymous
{
    template < class type >                                    concept default_initializable           = std::is_default_constructible          <type>::value; // std::default_initializable checks operator new, which does not accept cv-qualified ones.
    template < class type >                                    concept nothrow_default_initializable   = std::is_nothrow_default_constructible  <type>::value;
    template < class type >                                    concept trivially_default_initializable = std::is_trivially_default_constructible<type>::value;
    template < class type, class... types >                    concept constructible_from              = std::constructible_from                <type,types...>;
    template < class type, class... types >                    concept nothrow_constructible_from      = std::is_nothrow_constructible          <type,types...>::value;
    template < class type >                                    concept copyable                        = std::copyable                          <type>;
    template < class type >                                    concept nothrow_copyable                = std::is_nothrow_copy_constructible     <type>::value and std::is_nothrow_copy_assignable  <type>::value;
    template < class type >                                    concept trivially_copyable              = std::is_trivially_copy_constructible   <type>::value and std::is_trivially_copy_assignable<type>::value;
    template < class type >                                    concept movable                         = std::movable                           <type>;
    template < class type >                                    concept nothrow_movable                 = std::is_nothrow_move_constructible     <type>::value and std::is_nothrow_move_assignable  <type>::value;
    template < class type >                                    concept trivially_movable               = std::is_trivially_move_constructible   <type>::value and std::is_trivially_move_assignable<type>::value;
    template < class type >                                    concept destructible                    = std::destructible                      <type>;
    template < class type >                                    concept nothrow_destructible            = std::is_nothrow_destructible           <type>::value;
    template < class type >                                    concept trivially_destructible          = std::is_trivially_destructible         <type>::value;
    template < class type >                                    concept swappable                       = std::swappable                         <type>;
    template < class type >                                    concept nothrow_swappable               = std::is_nothrow_swappable              <type>::value;
    template < class type, class... types >                    concept invocable                       = std::invocable                         <type,types...>;
    template < class type, class result_type, class... types > concept invocable_r                     = std::is_invocable_r                    <result_type,type,types...>::value;
    template < class type, class type2 >                       concept predicate_for                   = std::predicate                         <type,type2>;
    template < class type, class type2, class type3 >          concept relation_between                = std::relation                          <type,type2,type3>;

    template < class type1, class type2 >                      concept same_as                         = std::same_as                           <type1,type2>;
    template < class type1, class type2 >                      concept base_of                         = std::derived_from                      <type2,type1>        and ( not std::same_as<type1,type2> ); // std::is_base_of allows private/protected extends, while std::derived_from does not.
    template < class type1, class type2 >                      concept derived_from                    = std::derived_from                      <type1,type2>        and ( not std::same_as<type1,type2> ); // std::derived_from<type,type> (where type is class or union) is true.
    template < class type1, class type2 >                      concept constructible_to                = std::constructible_from                <type2,type1>;
    template < class type1, class type2 >                      concept nothrow_constructible_to        = std::is_nothrow_constructible          <type2,type1>::value;
    template < class type1, class type2 >                      concept convertible_to                  = std::convertible_to                    <type1,type2>        and constructible_to        <type1,type2>; // Make convertible >= constructible.
    template < class type1, class type2 >                      concept nothrow_convertible_to          = std::is_nothrow_convertible            <type1,type2>::value and nothrow_constructible_to<type1,type2>; // Make convertible >= constructible.
    template < class type1, class type2 >                      concept assignable_from                 = std::assignable_from                   <type1,type2>;
    template < class type1, class type2 >                      concept nothrow_assignable_from         = std::is_nothrow_assignable             <type1,type2>::value;
    template < class type1, class type2 >                      concept swappable_with                  = std::swappable_with                    <type1,type2>;
    template < class type1, class type2 >                      concept nothrow_swappable_with          = std::is_nothrow_swappable_with         <type1,type2>::value;
    template < class type1, class type2 >                      concept common_with                     = std::common_with                       <type1,type2>;
    template < class type1, class type2 >                      concept common_reference_with           = std::common_reference_with             <type1,type2>;
    template < class type1, class type2 >                      concept layout_compatible_with          = std::is_layout_compatible              <type1,type2>::value; 
}