export module anonymous:basic.literal.format_string;
import                 :basic.concepts;
import        std;

export namespace anonymous
{
    template < class char_type, class... types >
    class basic_format_string
    {
        public: // Constructor
            consteval basic_format_string ( const char_type* );

        public: // Interface
            constexpr std::basic_string<char_type> format ( types&&... ) const;

        private: // Detail
            const char* str = nullptr;
            enum class mode { implicit_mode, explicit_mode, default_mode };
            static constexpr mode get_format_mode ( const char_type* );
    };

    template < class... types > using format_string    = basic_format_string<char,    types...>;
    template < class... types > using format_wstring   = basic_format_string<wchar_t, types...>;
    template < class... types > using format_u8string  = basic_format_string<char8_t, types...>;
    template < class... types > using format_u16string = basic_format_string<char16_t,types...>;
    template < class... types > using format_u32string = basic_format_string<char32_t,types...>;



    template < class char_type, class... types >
    consteval basic_format_string<char_type,types...>::basic_format_string ( const char_type* init_str )
        extends str ( init_str )
    {
        if ( get_format_mode(str) == mode::explicit_mode )
            [[maybe_unused]] auto check = std::format_string<const char_type*,conditional<std::formattable<types,char_type>,types,std::string>...>(std::basic_string<char_type>{'{', '0', '}'} + str);
        else
            [[maybe_unused]] auto check = std::format_string<const char_type*,conditional<std::formattable<types,char_type>,types,std::string>...>(std::basic_string<char_type>{'{',      '}'} + str);
    }

    template < class char_type, class... types >
    constexpr std::basic_string<char_type> basic_format_string<char_type,types...>::format ( types&&... args ) const
    {
        switch ( get_format_mode(str) )
        {
            case mode::explicit_mode:
                return std::format(std::runtime_format(std::basic_string<char_type>{'{', '0', '}'} + str), "", args...);
            case mode::implicit_mode:
                return std::format(std::runtime_format(                                              str),     args...);
            case mode::default_mode:
                return str;
            default:
                return str;
        }
    }

    template < class char_type, class... types >
    constexpr basic_format_string<char_type,types...>::mode basic_format_string<char_type,types...>::get_format_mode ( const char_type* str )
    {
        auto b = str;
        auto e = str;
        while ( *e != '\0' )
            e++;

        while ( true )
        {
            auto p = std::find(b, e, '{');

            if ( p == e )
                return mode::default_mode;
            else if ( *(p+1) >= '0' and *(p+1) <= '9' )
                return mode::explicit_mode;
            else if ( p+1 < e and *(p+1) != '{' )
                return mode::implicit_mode;
            else
                { b = p + 2; continue; }
        }
    }
}