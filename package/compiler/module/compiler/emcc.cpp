module;
#include <emscripten.h>

export module compiler:emcc;
export
{
    constexpr auto EM_LOG_C_STACK_  = EM_LOG_C_STACK;
    constexpr auto EM_LOG_JS_STACK_ = EM_LOG_JS_STACK;
    using ::emscripten_get_callstack;
}