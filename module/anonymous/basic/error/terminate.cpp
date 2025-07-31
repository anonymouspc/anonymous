export module anonymous:basic.error.terminate;
import                 :basic.error.detail.terminate_initializer;
import        std;

export namespace anonymous
{
    inline auto terminate_initializer = terminate_initializer_type();
}