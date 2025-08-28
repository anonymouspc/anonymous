export module anonymous:basic.literal.static_string;
import        std;

export namespace anonymous
{
    template < class char_type, int len >
    class basic_static_string
        extends public std::array<char_type,len>
    {
        public: // Constructor
            constexpr basic_static_string ( const char_type(&)[len] );
    };
    
    template < class char_type, int len1, int len2 > constexpr bool                 operator ==  ( const basic_static_string<char_type,len1>&, const basic_static_string<char_type,len2>& );
    template < class char_type, int len1, int len2 > constexpr std::strong_ordering operator <=> ( const basic_static_string<char_type,len1>&, const basic_static_string<char_type,len2>& );

    template < int len > using static_string    = basic_static_string<char,    len>;
    template < int len > using static_wstring   = basic_static_string<wchar_t, len>;
    template < int len > using static_u8string  = basic_static_string<char8_t, len>;
    template < int len > using static_u16string = basic_static_string<char16_t,len>;
    template < int len > using static_u32string = basic_static_string<char32_t,len>;

    

    template < class char_type, int len >
    constexpr basic_static_string<char_type,len>::basic_static_string ( const char_type (&init_str)[len] )
    {
        std::copy(std::begin(init_str), std::end(init_str), self.begin());
    }

    template < class char_type, int len1, int len2 >
    constexpr bool operator == ( const basic_static_string<char_type,len1>& left, const basic_static_string<char_type,len2>& right )
    {
        return std::equal(left.begin(), left.end(), right.begin(), right.end());
    }

    template < class char_type, int len1, int len2 >
    constexpr std::strong_ordering operator <=> ( const basic_static_string<char_type,len1>& left, const basic_static_string<char_type,len2>& right )
    {
        return std::lexicographical_compare_three_way(left.begin(), left.end(), right.begin(), right.end());
    }
}