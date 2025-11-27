module;
#include <cpptrace/cpptrace.hpp>

export module cpptrace;

export namespace cpptrace
{
    using cpptrace::frame_ptr;
    using cpptrace::generate_trace;
    using cpptrace::stacktrace;
    using cpptrace::stacktrace_frame;
}