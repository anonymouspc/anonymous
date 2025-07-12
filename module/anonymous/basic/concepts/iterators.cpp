export module anonymous:basic.concepts:iterators;
import        std;

export namespace anonymous
{
    template < class type > concept input_iterator           = std::input_iterator        <type>;
    template < class type > concept forward_iterator         = std::forward_iterator      <type>;
    template < class type > concept bidirectional_iterator   = std::bidirectional_iterator<type>;
    template < class type > concept random_access_iterator   = std::random_access_iterator<type>;
    template < class type > concept contiguous_iterator      = std::contiguous_iterator   <type>;

    template < class type > using   iterator_value_type      = std::iter_value_t          <type>;
    template < class type > using   iterator_reference       = std::iter_reference_t      <type>;
    template < class type > using   iterator_difference_type = std::iter_difference_t     <type>;

}