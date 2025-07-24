export module anonymous:basic.device.tbb.impl.container.queue;
import                 :basic.device.tbb.decl.tbb;
import                 :basic.error;
import        tbb;

export namespace anonymous
{
    template < class type >
    class tbb::queue
        extends public ::tbb::concurrent_queue<type>
    {
        public:
            void pop ( );
    };

    

    template < class type >
    void tbb::queue<type>::pop ( )
    {
        auto poped = type();
        bool success = ::tbb::concurrent_queue<type>::try_pop(poped);
        if ( not success )
            throw value_error("pop failed (with empty() = true)");
    }
}