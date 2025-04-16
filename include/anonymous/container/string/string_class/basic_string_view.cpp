#pragma once

template < class type, class device >
constexpr basic_string_view<type,device>::basic_string_view ( const_reference init )
    extends base ( &init, 1 )
{
    
}

template < class type, class device >
constexpr basic_string_view<type,device>::basic_string_view ( const_pointer init )
    extends base ( init )
{
    
}

template < class type, class device >
constexpr basic_string_view<type,device>::basic_string_view ( const_pointer init_data, int init_size )
    extends base ( init_data, init_size )
{

}

template < class type, class device >
constexpr basic_string_view<type,device>::basic_string_view ( const basic_string<type,device>& init ) 
    extends basic_string_view ( init.data(), init.size() )
{

}

template < class type, class device >
constexpr basic_string_view<type,device>::operator bool ( ) const
    requires same_as<type,char>
{
    return self == "true"  ? true  :
           self == "false" ? false :
                             throw value_error("cannot convert \"{}\" from {} into {}", self, typeid(self), typeid(bool));   
}

template < class type, class device >
template < number_type type2 >
constexpr basic_string_view<type,device>::operator type2 ( ) const
    requires same_as<type,char>
{
    auto cvt = type2();
    auto [p, ec] = std::from_chars ( data(), data() + size(), cvt );
    if ( p != data() + size() or ec != std::errc() )
        throw value_error("cannot convert \"{}\" from {} into {}", self, typeid(self), typeid(cvt));
    return cvt;
}

template < class type, class device >
template < inputable type2 >
constexpr basic_string_view<type,device>::operator type2 ( ) const
    requires same_as<type,char> and 
             ( not number_type<type2> ) and
             ( not string_type<type2> )
{
    auto cvt = type2();
    auto stream = std::stringstream();
    stream << self;
    stream >> cvt;
    if ( not stream.eof() and stream.fail() ) // Not until the stream reaches end, that the stream fails.
        throw value_error("cannot convert \"{}\" from {} into {}", self, typeid(self), typeid(cvt));
}

template < class type, class device >
constexpr int basic_string_view<type,device>::size ( ) const
{
    return base::size();
}

template < class type, class device >
constexpr bool basic_string_view<type,device>::empty ( ) const
{
    return base::empty();
}

template < class type, class device >
constexpr basic_string_view<type,device>::const_iterator basic_string_view<type,device>::begin ( ) const
{
    return data();
}

template < class type, class device >
constexpr basic_string_view<type,device>::const_iterator basic_string_view<type,device>::end ( ) const
{
    return data() + size();
}

template < class type, class device >
constexpr basic_string_view<type,device>::const_pointer basic_string_view<type,device>::data ( ) const
{
    return base::data();
}

template < class type, class device >
constexpr basic_string_view<type,device>::const_reference basic_string_view<type,device>::operator[] ( int pos ) const
{
    #ifdef debug
    if ( pos < -size() or pos == 0 or pos > size() )
        throw index_error("index {} is out of range with size {}", pos, size());
    #endif
    return base::operator[](pos >= 0 ? pos - 1 : pos + size());
}

template < class type, class device >
constexpr basic_string_view<type,device> basic_string_view<type,device>::operator[] ( int pos_1, int pos_2 ) const
{
    auto abs_pos_1 = pos_1 >= 0 ? pos_1 : pos_1 + size() + 1;
    auto abs_pos_2 = pos_2 >= 0 ? pos_2 : pos_2 + size() + 1;

    #ifdef debug
    if ( ( ( abs_pos_1 < 1 or abs_pos_1 > size() ) or
           ( abs_pos_2 < 1 or abs_pos_2 > size() ) )
    and not // Except for below:
         ( ( abs_pos_1 == size() + 1 or abs_pos_2 == 0 ) and abs_pos_1 == abs_pos_2 + 1 ) )
        throw index_error("index [{}, {}] is out of range with size {}", pos_1, pos_2, size());
    #endif

    return basic_string_view(data() + abs_pos_1 - 1, abs_pos_2 - abs_pos_1 + 1);
}

template < class type, class device >
constexpr bool basic_string_view<type,device>::ownership ( )
{
    return false;
}

template < class type, class device >
constexpr bool basic_string_view<type,device>::contiguous ( )
{
    return true;
}