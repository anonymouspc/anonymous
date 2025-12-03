export module std:extension.assert;
import           :extension.detail.compat;
import           :extension.stdio;

export
{
    void assert ( bool,                          std::source_location = std::source_location::current() );
    void assert ( bool, const char*,             std::source_location = std::source_location::current() );
    void assert ( bool, assert_printable auto&&, std::source_location = std::source_location::current() );
}



void assert ( bool condition, std::source_location location )
{
    assert(condition, "", location);
}

void assert ( bool condition, const char* message, std::source_location location )
{
    assert(condition, std::string_view(message), location);
}

void assert ( bool condition, assert_printable auto&& message, std::source_location location )
{
    if (not condition)
    {
        if (message.size() > 0)
            std::println(stderr, "assertion failed at {} in {}:{}:{}: {}", location.function_name(), location.file_name(), location.line(), location.column(), std::string_view(message.data(), message.size()));
        else
            std::println(stderr, "assertion failed at {} in {}:{}:{}",     location.function_name(), location.file_name(), location.line(), location.column());
        std::terminate();
    }
}