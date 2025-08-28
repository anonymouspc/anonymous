module anonymous:basic.error.detail.format_stacktrace;
import std;

namespace anonymous
{
    std::string format_stacktrace ( const std::stacktrace& );


 
    constexpr std::string_view red        = "\033[38;2;240;0;0m";
    constexpr std::string_view yellow     = "\033[38;2;240;240;0m";
    constexpr std::string_view green      = "\033[38;2;0;240;0m";
    constexpr std::string_view blue       = "\033[38;2;0;120;240m";
    constexpr std::string_view white      = "\033[38;2;192;192;192m";
    constexpr std::string_view light_grey = "\033[38;2;144;144;144m";
    constexpr std::string_view grey       = "\033[38;2;96;96;96m";
    constexpr std::string_view dark_grey  = "\033[38;2;48;48;48m";

    std::string format_stacktrace_color ( std::string str )
    {
        constexpr std::array<std::string_view,4> colors = { white, light_grey, grey, dark_grey };

        size_t pos = 0;
        size_t depth = 0;
        while ( true )
        {
            pos = std::min(str.find('<', pos), str.find('>', pos));

            if ( pos == str.npos )
                return str;
            
            else if ( str[pos] == '<' )
            {
                ++depth;
                auto color = colors[std::clamp(depth, 0uz, colors.size()-1)];
                str.insert(pos, color);
                pos += color.size() + 1;
            }

            else if ( str[pos] == '>' )
            {
                --depth;
                auto color = colors[std::clamp(depth, 0uz, colors.size()-1)];
                str.insert(pos, color);
                pos += color.size() + 1;
            }
        }
    }
    
    std::string format_stacktrace_module ( std::string str )
    {
        return std::regex_replace(str, std::regex(R"(@([\w\.]+|[\w\.]+:[\w\.]+))"), "");
    }

    std::string format_stacktrace ( const std::stacktrace& trace )
    {
        return trace | std::views::reverse
                     | std::views::transform([&] (const auto& entry)
                         {
                             if ( entry.source_file() != "" and entry.source_line() != 0 )
                                 return std::format("    {}{} {}{} {}{} {}{}:{}{}",
                                                    yellow, "at", white, format_stacktrace_color(format_stacktrace_module(entry.description())),
                                                    green,  "in", grey,  entry.source_file(), entry.source_line(),
                                                    white);
                             else
                                 return std::format("    {}{} {}{}{}",
                                                    yellow, "at", white, format_stacktrace_color(format_stacktrace_module(entry.description())),
                                                    white);
                         })
                     | std::views::join_with('\n')
                     | std::ranges::to<std::string>();
    }
}