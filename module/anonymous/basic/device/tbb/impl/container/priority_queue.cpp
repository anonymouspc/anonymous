export module anonymous:basic.device.tbb.impl.container.priority_queue;
import                 :basic.device.tbb.decl.tbb;
import                 :basic.error;
import        tbb;

export namespace anonymous
{
    template < class type, class compare >
    class tbb::priority_queue
        extends public ::tbb::concurrent_priority_queue<type,compare>
    {
        public:
            void pop ( );
    };

    

    template < class type, class compare >
    void tbb::priority_queue<type,compare>::pop ( )
    {
        auto poped = type();
        bool success = ::tbb::concurrent_priority_queue<type,compare>::try_pop(poped);
        if ( not success )
            throw value_error("pop failed (with empty() = true)");
    }
}