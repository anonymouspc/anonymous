export module anonymous:basic.error.detail.stringify_stacktrace;
import        std;

export namespace anonymous
{
    constexpr const char* red        = "\033[38;2;240;0;0m";
    constexpr const char* yellow     = "\033[38;2;240;240;0m";
    constexpr const char* green      = "\033[38;2;0;240;0m";
    constexpr const char* blue       = "\033[38;2;0;120;240m";
    constexpr const char* white      = "\033[38;2;192;192;192m";
    constexpr const char* light_grey = "\033[38;2;144;144;144m";
    constexpr const char* grey       = "\033[38;2;96;96;96m";
    constexpr const char* dark_grey  = "\033[38;2;48;48;48m";

    std::string stringify_stacktrace        ( const std::stacktrace& );
    std::string stringify_stacktrace_color  ( std::string, int = 0, int = 0 );
    std::string stringify_stacktrace_module ( std::string );


    
    std::string stringify_stacktrace ( const std::stacktrace& trace )
    {
        return trace | std::views::reverse
                     | std::views::transform([&] (const auto& entry)
                         {
                             if ( entry.source_file() != "" and entry.source_line() != 0 )
                                 return std::format("    {}{} {}{} {}{} {}{}:{}{}",
                                                    yellow, "at", white, stringify_stacktrace_color(stringify_stacktrace_module(entry.description())),
                                                    green,  "in", grey,  entry.source_file(), entry.source_line(),
                                                    white);
                             else
                                 return std::format("    {}{} {}{}{}",
                                                    yellow, "at", white, stringify_stacktrace_color(stringify_stacktrace_module(entry.description())),
                                                    white);
                         })
                     | std::views::join_with('\n')
                     | std::ranges::to<std::string>();
    }
    
    std::string stringify_stacktrace_color ( std::string str, int str_pos, int colors_pos )
    {
        constexpr std::array<const char*,4> colors = { white, light_grey, grey, dark_grey };
    
        // Locate brackets
        auto p1 = str.find('<', str_pos);
        auto p2 = str.find('>', str_pos);
    
        // Find end.
        if ( p1 == str.npos and p2 == str.npos )
            return str;
    
        // '<' is first.
        if ( p1 != str.npos and p1 < p2 )
        {
            int p = std::clamp(++colors_pos, 0, int(colors.size()-1));
            str.insert(p1, colors[p]);
            str_pos = p1 + std::string_view(colors[p]).size() + 1;
        }
    
        // '>' is first.
        else if ( p2 != str.npos and p2 < p1 )
        {
            int p = std::clamp(--colors_pos, 0, int(colors.size()-1));
            str.insert(p2 + 1, colors[p]);
            str_pos = p2 + 1 + std::string_view(colors[p]).size();
        }
    
        // Continue.
        return stringify_stacktrace_color ( std::move(str), str_pos, colors_pos );
    }
    
    std::string stringify_stacktrace_module ( std::string str )
    {
        return std::regex_replace(str, std::regex(R"(@([\w\.]+|[\w\.]+:[\w\.]+))"), "");
    }
}