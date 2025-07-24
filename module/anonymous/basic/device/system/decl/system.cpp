export module anonymous:basic.device.system.decl.system;
import                 :basic.device.system.decl.detail.system_context;
import        std;

export namespace anonymous
{
    class system
    {
        public: // Execution
            using execution_context_type = system_context;
            inline static execution_context_type execution_context = execution_context_type();

        public: // Random
            using random_context_type = std::random_device;
            inline static thread_local random_context_type random_context = random_context_type();
    };
}