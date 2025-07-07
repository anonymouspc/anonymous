export module anonymous.basic.concepts.convert;
import std;

export namespace anonymous
{
    template < class type >                               using add_const              = std::add_const              <type>                 ::type;
    template < class type >                               using add_cv                 = std::add_cv                 <type>                 ::type;
    template < class type >                               using add_lvalue_reference   = std::add_lvalue_reference   <type>                 ::type;
    template < class type >                               using add_pointer            = std::add_pointer            <type>                 ::type;
    template < class type >                               using add_rvalue_reference   = std::add_rvalue_reference   <type>                 ::type;
    template < class type >                               using add_volatile           = std::add_volatile           <type>                 ::type;
    template < class type, class... types >               using basic_common_reference = std::basic_common_reference <type,types...>        ::type;
    template < class type, class... types >               using common_type            = std::common_type            <type,types...>        ::type;
    template < class type, class... types >               using common_reference       = std::common_reference       <type,types...>        ::type;
    template < bool condition, class type1, class type2 > using conditional            = std::conditional            <condition,type1,type2>::type;
    template < class type >                               using decay                  = std::decay                  <type>                 ::type;
    template < class type, class... types >               using invoke_result          = std::invoke_result          <type,types...>        ::type;
    template < class type >                               using make_signed            = std::make_signed            <type>                 ::type;
    template < class type >                               using make_unsigned          = std::make_unsigned          <type>                 ::type;
    template < class type >                               using remove_all_extents     = std::remove_all_extents     <type>                 ::type;
    template < class type >                               using remove_const           = std::remove_const           <type>                 ::type;
    template < class type >                               using remove_cv              = std::remove_cv              <type>                 ::type;
    template < class type >                               using remove_cvref           = std::remove_cvref           <type>                 ::type;
    template < class type >                               using remove_volatile        = std::remove_volatile        <type>                 ::type;
    template < class type >                               using remove_extent          = std::remove_extent          <type>                 ::type;
    template < class type >                               using remove_pointer         = std::remove_pointer         <type>                 ::type;
    template < class type >                               using remove_reference       = std::remove_reference       <type>                 ::type;
    template < class type >                               using type_identity          = std::type_identity          <type>                 ::type;
}