#pragma once

} // Out of namespace anonymous

template < anonymous::string_type type >  
struct std::hash<type>
    extends public type::device_type::template hash<typename type::device_type::template basic_string_view<typename type::value_type>>
{
    constexpr auto operator() ( const type& ) const;
};

#include "hash.ipp"

namespace anonymous { // Back into namespace anonymous