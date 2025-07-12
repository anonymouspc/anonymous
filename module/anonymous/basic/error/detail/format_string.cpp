export module anonymous:basic.error.detail.format_string;
import        anonymous.basic.concepts;
import        std;

export namespace anonymous
{
    template < class... types >
    class format_string
    {
        public: // Interface
            consteval format_string ( const char* );
            constexpr std::string format ( types&&... ) const;

        private: // Detail
            const char* str = nullptr;
            enum class mode { implicit_mode, explicit_mode, default_mode };
            constexpr static mode get_format_mode ( const char* );
    };



    template < class... types >
    consteval format_string<types...>::format_string ( const char* init_str )
        extends str ( init_str )
    {
        if ( get_format_mode(str) == mode::explicit_mode )
            /*check-only*/ (void) std::format_string<const char*,conditional<std::formattable<types,char>,types,std::string>...>(std::string("{0}") + str);
        else
            /*check-only*/ (void) std::format_string<const char*,conditional<std::formattable<types,char>,types,std::string>...>(std::string("{}" ) + str);
    }

    template < class... types >
    constexpr std::string format_string<types...>::format ( types&&... args ) const
    {
        switch ( get_format_mode(str) )
        {
            case mode::explicit_mode:
                return std::format(std::runtime_format(std::string("{0}") + str), "", args...);
            case mode::implicit_mode:
                return std::format(std::runtime_format(                     str),     args...);
            case mode::default_mode:
                return str;
            default:
                return str;
        }
    }

    template < class... types >
    constexpr format_string<types...>::mode format_string<types...>::get_format_mode ( const char* str )
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