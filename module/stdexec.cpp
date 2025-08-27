module;
#undef in
#undef self
#define __cpp_lib_execution false
#include <stdexec/concepts.hpp>
#include <stdexec/coroutine.hpp>
#include <stdexec/execution.hpp>
#include <stdexec/functional.hpp>
#include <stdexec/stop_token.hpp>

export module stdexec;
// import std; This module might be depended by std:feature.sender by std:feature by std.

export namespace stdexec 
{ 
    using stdexec::completion_signatures;
    using stdexec::forward_progress_guarantee;
    using stdexec::get_completion_scheduler;
    // using stdexec::get_completion_scheduler_t;
    // using stdexec::get_env;
    // using stdexec::get_env_t;
    // using stdexec::get_forward_progress_guarantee_t;
    // using stdexec::get_scheduler_t;
    // using stdexec::get_stop_token;
    // using stdexec::just;
    // using stdexec::operation_state;
    // using stdexec::receiver;
    // using stdexec::receiver_of;
    // using stdexec::schedule;
    // using stdexec::scheduler;
    // using stdexec::set_error;
    // using stdexec::set_error_t;
    // using stdexec::set_stopped;
    // using stdexec::set_stopped_t;
    // using stdexec::set_value;
    // using stdexec::set_value_t;
    // using stdexec::sender;
    // using stdexec::sender_of;
    // using stdexec::sender_in;
    // using stdexec::sender_to;
    // using stdexec::sender_t;
    // using stdexec::split;
    // using stdexec::sync_wait;
    // using stdexec::then;

    // using stdexec::__call_result_t;
    // using stdexec::__sender_adaptor_closure;
    // using stdexec::__sender_adaptor_closure_for;
    // using ::operator|;
    // using stdexec::__closure::operator|;
}
