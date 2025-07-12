export module anonymous:basic.concepts:ranges;
import        std;

export namespace anonymous
{
    template < class type > concept input_range           = std::ranges::input_range        <type>;
    template < class type > concept forward_range         = std::ranges::forward_range      <type>;
    template < class type > concept bidirectional_range   = std::ranges::bidirectional_range<type>;
    template < class type > concept random_access_range   = std::ranges::random_access_range<type>;
    template < class type > concept contiguous_range      = std::ranges::contiguous_range   <type>;

    template < class type > using   range_value_type      = std::ranges::range_value_t     <type>;
    template < class type > using   range_reference       = std::ranges::range_reference_t <type>;
    template < class type > using   range_difference_type = std::ranges::range_difference_t<type>;                       
    template < class type > using   range_iterator        = std::ranges::iterator_t        <type>; 
    template < class type > using   range_const_iterator  = std::ranges::const_iterator_t  <type>;
    template < class type > using   range_sentinel        = std::ranges::sentinel_t        <type>; 
    template < class type > using   range_const_sentinel  = std::ranges::const_sentinel_t  <type>;

}