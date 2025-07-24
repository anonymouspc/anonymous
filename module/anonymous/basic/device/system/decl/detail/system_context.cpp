export module anonymous:basic.device.system.decl.detail.system_context;
import        std;
import        boost.asio;

export namespace anonymous
{
    class system_context
    {
        private: // Typedef
            class scheduler;
        
        public: // Interface
            static constexpr std::execution::scheduler auto get_scheduler ( ) noexcept;
    };

    

    class system_context::scheduler
    {
        private: // Typedef
             class sender;

        public: // Interface
            static constexpr std::execution::sender auto schedule ( ) noexcept;

        public: // Query
            static constexpr auto query ( std::execution::get_env_t )                        noexcept;
            static constexpr auto query ( std::execution::get_forward_progress_guarantee_t ) noexcept;

        public: // Operator
            friend constexpr bool operator == ( const scheduler&, const scheduler& ) = default;

        private:
            [[maybe_unused]] int i_am_not_constexpr = 42;
    };

    class system_context::scheduler::sender
    {
        private: // Typedef
            template < class receiver > class operation_state;

        public: // Traits
            using sender_concept        = std::execution::sender_t;
            using completion_signatures = std::execution::completion_signatures<std::execution::set_value_t()>;

        public: // Interface
            static constexpr std::execution::operation_state auto connect ( std::execution::receiver auto&& );

        public: // Query
                                            static constexpr auto query ( std::execution::get_env_t )                                noexcept;
                                            static constexpr auto query ( std::execution::get_scheduler_t )                          noexcept;
            template < class channel_type > static constexpr auto query ( std::execution::get_completion_scheduler_t<channel_type> ) noexcept;
            
        private:
            [[maybe_unused]] int i_am_not_constexpr = 42;
    };

    template < class receiver >
    class system_context::scheduler::sender::operation_state
    {
        public: // Constructor
            constexpr operation_state ( receiver );

        public: // Interface
            constexpr void start ( ) noexcept;

        private: // Data
            receiver recv = receiver();
    };

    template < class receiver >
    constexpr system_context::scheduler::sender::operation_state<receiver>::operation_state ( receiver init_recv )
        extends recv ( std::move(init_recv) )
    {

    }

    template < class receiver >
    constexpr void system_context::scheduler::sender::operation_state<receiver>::start ( ) noexcept
    {
        if ( not std::execution::get_stop_token(std::execution::get_env(recv)).stop_requested() )
            try
            {
                boost::asio::post(boost::asio::system_executor(), [&] { std::execution::set_value(std::move(recv)); }); // Value channel.
            }
            catch (...)
            {
                std::execution::set_error(std::move(recv), std::current_exception()); // Error channel.
            }
        else
            std::execution::set_stopped(std::move(recv)); // Stop channel.
    }

    constexpr std::execution::operation_state auto system_context::scheduler::sender::connect ( std::execution::receiver auto&& recv )
    {
        return operation_state(std::forward<decltype(recv)>(recv));
    }

    constexpr auto system_context::scheduler::sender::query ( std::execution::get_env_t ) noexcept
    {
        return sender();
    }

    constexpr auto system_context::scheduler::sender::query ( std::execution::get_scheduler_t ) noexcept
    {
        return scheduler();
    } 

    template < class channel_type >
    constexpr auto system_context::scheduler::sender::query ( std::execution::get_completion_scheduler_t<channel_type> ) noexcept
    {
        return scheduler();
    }

    constexpr std::execution::sender auto system_context::scheduler::schedule ( ) noexcept
    {
        return sender();
    }

    constexpr auto system_context::scheduler::query ( std::execution::get_env_t ) noexcept
    {
        return scheduler();
    }

    constexpr auto system_context::scheduler::query ( std::execution::get_forward_progress_guarantee_t ) noexcept
    {
        return std::execution::forward_progress_guarantee::concurrent;
    }
    
    constexpr std::execution::scheduler auto system_context::get_scheduler ( ) noexcept
    {
        return scheduler();
    }
}