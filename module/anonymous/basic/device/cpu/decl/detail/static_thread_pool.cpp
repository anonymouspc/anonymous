export module anonymous:basic.device.cpu.decl.detail.static_thread_pool;
import        std;

export namespace anonymous
{
    class static_thread_pool
    {
        private: // Typedef
            class scheduler;

        public: // Constructor
            static_thread_pool ( int );

        public: // Interface
            std::execution::scheduler auto get_scheduler ( ) const noexcept;
    };
}