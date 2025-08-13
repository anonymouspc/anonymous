export module anonymous:basic.error.terminate;
import                 :basic.error.detail.format_stacktrace;
import        std;

export namespace anonymous
{
    struct terminate_initializer_type
    {
        terminate_initializer_type ( );  
    };

    inline auto terminate_initializer = terminate_initializer_type();



    terminate_initializer_type::terminate_initializer_type ( )
    {
        static auto handler = std::get_terminate();

        std::set_terminate([]
            {
                std::cerr << format_stacktrace(std::stacktrace::current()) << std::endl;
                handler();
            });
    }
}