export module anonymous:basic.concepts.traits;
import        std;

export namespace anonymous
{
    template < class type >                               constexpr bool is_abstract                = std::is_abstract               <type>                 ::value;
    template < class type >                               constexpr bool is_aggregate               = std::is_aggregate              <type>                 ::value;
    template < class type >                               constexpr bool is_array                   = std::is_array                  <type>                 ::value;
    template < class type, class type2 >                  constexpr bool is_assignable              = std::is_assignable             <type,type2>           ::value;
    template < class type >                               constexpr bool is_bounded_array           = std::is_bounded_array          <type>                 ::value;
    template < class type >                               constexpr bool is_class                   = std::is_class                  <type>                 ::value;
    template < class type >                               constexpr bool is_const                   = std::is_const                  <type>                 ::value;
    template < class type >                               constexpr bool is_empty                   = std::is_empty                  <type>                 ::value;
    template < class type >                               constexpr bool is_enum                    = std::is_enum                   <type>                 ::value;
    template < class type >                               constexpr bool is_final                   = std::is_final                  <type>                 ::value;
    template < class type >                               constexpr bool is_function                = std::is_function               <type>                 ::value;
    template < class type >                               constexpr bool is_lvalue_reference        = std::is_lvalue_reference       <type>                 ::value;
    template < class type >                               constexpr bool is_member_object_pointer   = std::is_member_object_pointer  <type>                 ::value;
    template < class type >                               constexpr bool is_member_pointer          = std::is_member_pointer         <type>                 ::value;
    template < class type >                               constexpr bool is_member_function_pointer = std::is_member_function_pointer<type>                 ::value;
    template < class type >                               constexpr bool is_null_pointer            = std::is_null_pointer           <type>                 ::value;
    template < class type >                               constexpr bool is_object                  = std::is_object                 <type>                 ::value;
    template < class type >                               constexpr bool is_pointer                 = std::is_pointer                <type>                 ::value;
    template < class type >                               constexpr bool is_polymorphic             = std::is_polymorphic            <type>                 ::value;
    template < class type >                               constexpr bool is_reference               = std::is_reference              <type>                 ::value;
    template < class type >                               constexpr bool is_rvalue_reference        = std::is_rvalue_reference       <type>                 ::value;
    template < class type, class type2 >                  constexpr bool is_same                    = std::is_same                   <type,type2>           ::value;
    template < class type >                               constexpr bool is_standard_layout         = std::is_standard_layout        <type>                 ::value;
    template < class type >                               constexpr bool is_unbounded_array         = std::is_unbounded_array        <type>                 ::value;
    template < class type >                               constexpr bool is_union                   = std::is_union                  <type>                 ::value;
    template < class type >                               constexpr bool is_void                    = std::is_void                   <type>                 ::value;
    template < class type >                               constexpr bool is_volatile                = std::is_volatile               <type>                 ::value;

    template < class type >                               using          add_const                  = std::add_const                 <type>                 ::type;
    template < class type >                               using          add_cv                     = std::add_cv                    <type>                 ::type;
    template < class type >                               using          add_lvalue_reference       = std::add_lvalue_reference      <type>                 ::type;
    template < class type >                               using          add_pointer                = std::add_pointer               <type>                 ::type;
    template < class type >                               using          add_rvalue_reference       = std::add_rvalue_reference      <type>                 ::type;
    template < class type >                               using          add_volatile               = std::add_volatile              <type>                 ::type;
    template < class type, class... types >               using          basic_common_reference     = std::basic_common_reference    <type,types...>        ::type;
    template < class type, class... types >               using          common_type                = std::common_type               <type,types...>        ::type;
    template < class type, class... types >               using          common_reference           = std::common_reference          <type,types...>        ::type;
    template < bool condition, class type1, class type2 > using          conditional                = std::conditional               <condition,type1,type2>::type;
    template < class type >                               using          decay                      = std::decay                     <type>                 ::type;
    template < class type, class... types >               using          invoke_result              = std::invoke_result             <type,types...>        ::type;
    template < class type >                               using          make_signed                = std::make_signed               <type>                 ::type;
    template < class type >                               using          make_unsigned              = std::make_unsigned             <type>                 ::type;
    template < class type >                               using          remove_all_extents         = std::remove_all_extents        <type>                 ::type;
    template < class type >                               using          remove_const               = std::remove_const              <type>                 ::type;
    template < class type >                               using          remove_cv                  = std::remove_cv                 <type>                 ::type;
    template < class type >                               using          remove_cvref               = std::remove_cvref              <type>                 ::type;
    template < class type >                               using          remove_volatile            = std::remove_volatile           <type>                 ::type;
    template < class type >                               using          remove_extent              = std::remove_extent             <type>                 ::type;
    template < class type >                               using          remove_pointer             = std::remove_pointer            <type>                 ::type;
    template < class type >                               using          remove_reference           = std::remove_reference          <type>                 ::type;
    template < class type >                               using          type_identity              = std::type_identity             <type>                 ::type;
}