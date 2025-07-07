export module anonymous.basic.concepts.trait;
import std;

export namespace anonymous
{
    template < class type >              constexpr bool is_abstract                = std::is_abstract                <type>      ::value;
    template < class type >              constexpr bool is_aggregate               = std::is_aggregate               <type>      ::value;
    template < class type >              constexpr bool is_array                   = std::is_array                   <type>      ::value;
    template < class type, class type2 > constexpr bool is_assignable              = std::is_assignable              <type,type2>::value;
    template < class type >              constexpr bool is_bounded_array           = std::is_bounded_array           <type>      ::value;
    template < class type >              constexpr bool is_class                   = std::is_class                   <type>      ::value;
    template < class type >              constexpr bool is_const                   = std::is_const                   <type>      ::value;
    template < class type >              constexpr bool is_empty                   = std::is_empty                   <type>      ::value;
    template < class type >              constexpr bool is_enum                    = std::is_enum                    <type>      ::value;
    template < class type >              constexpr bool is_final                   = std::is_final                   <type>      ::value;
    template < class type >              constexpr bool is_function                = std::is_function                <type>      ::value;
    template < class type >              constexpr bool is_lvalue_reference        = std::is_lvalue_reference        <type>      ::value;
    template < class type >              constexpr bool is_member_object_pointer   = std::is_member_object_pointer   <type>      ::value;
    template < class type >              constexpr bool is_member_pointer          = std::is_member_pointer          <type>      ::value;
    template < class type >              constexpr bool is_member_function_pointer = std::is_member_function_pointer <type>      ::value;
    template < class type >              constexpr bool is_null_pointer            = std::is_null_pointer            <type>      ::value;
    template < class type >              constexpr bool is_object                  = std::is_object                  <type>      ::value;
    template < class type >              constexpr bool is_pointer                 = std::is_pointer                 <type>      ::value;
    template < class type >              constexpr bool is_polymorphic             = std::is_polymorphic             <type>      ::value;
    template < class type >              constexpr bool is_reference               = std::is_reference               <type>      ::value;
    template < class type >              constexpr bool is_rvalue_reference        = std::is_rvalue_reference        <type>      ::value;
    template < class type, class type2 > constexpr bool is_same                    = std::is_same                    <type,type2>::value;
    template < class type >              constexpr bool is_standard_layout         = std::is_standard_layout         <type>      ::value;
    template < class type >              constexpr bool is_unbounded_array         = std::is_unbounded_array         <type>      ::value;
    template < class type >              constexpr bool is_union                   = std::is_union                   <type>      ::value;
    template < class type >              constexpr bool is_void                    = std::is_void                    <type>      ::value;
    template < class type >              constexpr bool is_volatile                = std::is_volatile                <type>      ::value;
}