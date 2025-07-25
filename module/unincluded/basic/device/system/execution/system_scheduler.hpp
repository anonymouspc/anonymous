class system_scheduler
{
    private: // Core
        constexpr system_scheduler ( ) = default;
        friend class system_context;

    private: // Typedef
                                                                          class sender;
        template < class sender_type, class shape_type, class func_type > class bulk_sender;

    public: // Interface
        static constexpr std::execution::sender auto schedule ( )                                                        noexcept;  
        static constexpr std::execution::sender auto bulk     ( std::execution::sender auto&&, integral auto&&, auto&& ) noexcept;

    public: // Query
        static constexpr auto query ( std::execution::get_env_t )                        noexcept;
        static constexpr auto query ( std::execution::get_forward_progress_guarantee_t ) noexcept;

    public: // Operator
        friend constexpr bool operator == ( const system_scheduler&, const system_scheduler& ) = default;

    private: // Data
        [[maybe_unused]] int i_am_not_constexpr = 42;
};

#include "system_scheduler.cpp"

