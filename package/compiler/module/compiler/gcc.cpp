module;
#include <cxxabi.h>
#include <unwind.h>

export module compiler:gcc;
export
{
    using ::_Unwind_Backtrace;
    using ::_Unwind_Context;
    using ::_Unwind_GetIP;
    using ::_URC_END_OF_STACK;
    using ::_URC_NO_REASON;
    using ::__cxxabiv1::__cxa_demangle;
}
