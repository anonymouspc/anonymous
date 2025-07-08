export module anonymous.basic.error:exception;
import                             :detail.format_string;
import                             :detail.stringify_stacktrace;
import        anonymous.basic.concepts;
import        std;

export namespace anonymous
{
    class exception;
        class logic_error;
            class value_error;
                class index_error;
                class key_error;
            class type_error;

        class runtime_error;
            class text_error;
                class encode_error;
                class format_error;
                class parse_error;
                class regex_error;
            class io_error;
                class file_error;
                class pipe_error;
                class serial_port_error;
                class network_error;
                class mysql_error;
            class math_error;
                class linalg_error;

        class internal_error;

        class signal;
            class abort_signal;
            class floating_point_exception_signal;
            class illegal_instruction_signal;
            class interrupt_signal;
            class segmentation_violation_signal;
            class terminate_signal;

    class exception
        extends public std::exception
    {
        public: // Core
            exception ( ) = default;
            exception ( const exception& );
            template < class... types > exception ( format_string<type_identity<types>...>, types&&... );

        public: // Member
            virtual const char* what ( ) const noexcept;

        protected: // Data
            mutable std::string     error_what       = "";
                    std::string     error_message    = "";
                    std::stacktrace error_stacktrace = std::stacktrace::current();
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

    class index_error
        extends public value_error
    {
        public:
            using value_error::value_error;
    };

    class key_error
        extends public value_error
    {
        public:
            using value_error::value_error;
    };

    class type_error
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

    class text_error
        extends public runtime_error
    {
        public:
            using runtime_error::runtime_error;
    };

    class encode_error
        extends public text_error
    {
        public:
            using text_error::text_error;
    };

    class format_error
        extends public text_error
    {
        public:
            using text_error::text_error;
    };

    class parse_error
        extends public text_error
    {
        public:
            using text_error::text_error;
    };

    class regex_error
        extends public text_error
    {
        public:
            using text_error::text_error;
    };

    class io_error
        extends public runtime_error
    {
        public:
            using runtime_error::runtime_error;
    };

    class file_error
        extends public io_error
    {
        public:
            using io_error::io_error;
    };

    class pipe_error
        extends public io_error
    {
        public:
            using io_error::io_error;
    };

    class serial_port_error
        extends public io_error
    {
        public:
            using io_error::io_error;
    };

    class network_error
        extends public io_error
    {
        public:
            using io_error::io_error;
    };

    class math_error
        extends public runtime_error
    {
        public:
            using runtime_error::runtime_error;
    };

    class linalg_error
        extends public math_error
    {
        public:
            using math_error::math_error;
    };

    class internal_error
        extends public exception
    {
        public:
            internal_error ( ) = default; // An internal error must not carry message.
    };

    class signal
        extends public exception
    {
        using exception::exception;
    };

    class abort_signal
        extends public signal
    {
        using signal::signal;  
    };

    class floating_point_exception_signal
        extends public signal
    {
        using signal::signal;
    };

    class illegal_instruction_signal
        extends public signal
    {
        using signal::signal;
    };

    class interrupt_signal
        extends public signal
    {
        using signal::signal;
    };

    class segmentation_violation_signal
        extends public signal
    {
        using signal::signal;
    };

    class terminate_signal
        extends public signal
    {
        using signal::signal;
    };



    template < class... types >
    exception::exception ( format_string<type_identity<types>...> str, types&&... args )
        extends error_message ( str.format(std::forward<decltype(args)>(args)...) )
    {
        
    }

    const char* exception::what ( ) const noexcept
    {
        error_what = red   + error_message + '\n' +
                     white + stringify_stacktrace(error_stacktrace);
            
        return error_what.c_str();
    }
}