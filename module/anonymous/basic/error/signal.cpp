export module anonymous:basic.error.signal;
import                 :basic.error.detail.signal_initializer;
import        std;

export namespace anonymous
{
    inline auto signal_initializer = signal_initializer_type();
}

