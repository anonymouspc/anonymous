module std:feature.stacktrace.gcc;
import    :compiler;
import compiler;
import system;

namespace std
{
    using native_stacktrace_entry = void*;

    std::ranges::forward_range auto native_stacktrace_current ( )
    {
        auto trace = std::vector<native_stacktrace_entry>();
        auto callback = [&] (_Unwind_Context* ctx)
            {
                uintptr_t pc = _Unwind_GetIP(ctx);
                if (pc > 0)
                {
                    trace.push_back(reinterpret_cast<native_stacktrace_entry>(pc));
                    return _URC_NO_REASON;
                }
                else
                    return _URC_END_OF_STACK;
            };
        _Unwind_Backtrace([] (_Unwind_Context* ctx, void* callback_ptr) { return (*static_cast<decltype(callback)*>(callback_ptr))(ctx); }, &callback);
        return trace;
    }

    std::string native_stacktrace_entry_description ( const native_stacktrace_entry& entry )
    {
        if (entry != nullptr)
        {
            auto info = Dl_info();
            auto addressed = dladdr(entry, &info);
            if (addressed and info.dli_sname != nullptr)
                return info.dli_sname;
            else
                return "";
        }
        else
            return "";
    }

    std::string native_stacktrace_entry_source_file ( const native_stacktrace_entry& entry )
    {
        return "";
    }

    int native_stacktrace_entry_source_line ( const native_stacktrace_entry& entry )
    {
        return 0;
    }
}