export module anonymous:basic.error.exception;
import                 :basic.concepts;
import                 :basic.utility;
import        std;

export namespace anonymous
{
    class exception;
        class logic_error;
            class value_error;
        class runtime_error;
        class signal;

    class exception
        extends public std::exception
    {
        public: // Core
            exception ( ) = default;
            exception ( const exception& );
            template < class... types > exception ( format_string<type_identity<types>...>, types&&... );

        public: // Member
            virtual const char* what ( ) const noexcept;

        private: // Data
            std::string message = "";
    };

    class logic_error
        extends public exception
    {
        public:
            using exception::exception;
    };

    class value_error
        extends public logic_error
    {
        public:
            using logic_error::logic_error;
    };

    class runtime_error
        extends public exception
    {
        public:
            using exception::exception;
            runtime_error ( ) = delete; // A runtime error must carry message.
    };

    class signal
        extends public exception
    {
        using exception::exception;
    };



    template < class... types >
    exception::exception ( format_string<type_identity<types>...> str, types&&... args )
        extends message ( str.format(std::forward<decltype(args)>(args)...) )
    {
        
    }

    const char* exception::what ( ) const noexcept
    {
        return message.c_str();
    }
}