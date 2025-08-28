export module anonymous:basic.device.cpu.impl.execution.execution_context_type;
import                 :basic.device.cpu.decl;
import        std;

export namespace anonymous
{
    class cpu::execution_context_type
    {
        private: // Typedef
            class scheduler;

        public: // Constructor
            execution_context_type ( int ) { };

        public: // Interface
            std::execution::scheduler auto get_scheduler ( ) const noexcept;
    };
}