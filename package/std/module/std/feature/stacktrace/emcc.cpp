module std:feature.stacktrace.emcc;
import    :compiler;
import compiler;

namespace std
{
    using native_stacktrace_entry = std::string;

    std::ranges::forward_range auto native_stacktrace_current ( )
    {
        auto str = std::string();
        for (size_t size = 1024; size <= 65536; size *= 4)
        {
            str.resize(size);
            int bytes_got = emscripten_get_callstack(EM_LOG_C_STACK_ | EM_LOG_JS_STACK_, str.data(), str.size());
            str.resize(bytes_got);
            if (bytes_got < size)
                break;
        }
        return str | std::views::split('\n') | std::ranges::to<std::vector<native_stacktrace_entry>>();
    }

    std::string native_stacktrace_entry_description ( const native_stacktrace_entry& entry )
    {
        return entry;
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