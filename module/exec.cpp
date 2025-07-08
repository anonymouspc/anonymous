module;
#undef in
#undef self
#define __cpp_lib_execution false
#include <exec/static_thread_pool.hpp>
#include <exec/when_any.hpp>

export module exec;
import std;
import stdexec;

export namespace exec
{
    using exec::static_thread_pool;
    using exec::when_any;
}