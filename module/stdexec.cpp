module;
#undef in
#undef self
#include <beman/execution/execution.hpp>
#include <beman/execution/functional.hpp>
#include <beman/execution/stop_token.hpp>
#include <beman/execution/detail/just.hpp>

export module stdexec;
// import std; This module might be depended by std:feature.sender by std:feature by std.

export namespace stdexec
{
    using beman::execution::completion_signatures;
 // using beman::execution::forward_progress_guarantee;
    using beman::execution::get_completion_scheduler;
    using beman::execution::get_completion_scheduler_t;
    using beman::execution::get_env;
    using beman::execution::get_env_t;
 // using beman::execution::get_forward_progress_guarantee_t;
    using beman::execution::get_scheduler_t;
    using beman::execution::get_stop_token;
    using beman::execution::just;
    using beman::execution::operation_state;
    using beman::execution::receiver;
    using beman::execution::receiver_of;
    using beman::execution::schedule;
    using beman::execution::scheduler;
    using beman::execution::set_error;
    using beman::execution::set_error_t;
    using beman::execution::set_stopped;
    using beman::execution::set_stopped_t;
    using beman::execution::set_value;
    using beman::execution::set_value_t;
    using beman::execution::sender;
    using beman::execution::sender_in;
 // using beman::execution::sender_to;
    using beman::execution::sender_t;
    using beman::execution::sync_wait;
    using beman::execution::then;
} 