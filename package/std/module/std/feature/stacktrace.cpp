export module std:feature.stacktrace;
#ifdef __EMSCRIPTEN__
import           :feature.stacktrace.emcc;
#elifdef __GNUC__
import           :feature.stacktrace.gcc;
#endif




export namespace std
{
    class stacktrace_entry
    {
        public:
            using native_handle_type = native_stacktrace_entry;

        public:
            constexpr stacktrace_entry ( )                         noexcept;
            constexpr stacktrace_entry ( native_handle_type )      noexcept;
            constexpr stacktrace_entry ( const stacktrace_entry& ) noexcept;

        public:
            constexpr native_handle_type native_handle ( ) const noexcept;
            constexpr explicit operator bool           ( ) const noexcept;
            
        public:
            std::string         description ( ) const;
            std::string         source_file ( ) const;
            std::uint_least32_t source_line ( ) const;

        private:
            native_handle_type handle = native_handle_type();
    };

    constexpr bool                 operator ==  ( const stacktrace_entry&, const stacktrace_entry& ) noexcept;
    constexpr std::strong_ordering operator <=> ( const stacktrace_entry&, const stacktrace_entry& ) noexcept;
              std::ostream&        operator <<  (       std::ostream&,     const stacktrace_entry& );
              std::string          to_string    (                          const stacktrace_entry& );

    template < class allocator >
    class basic_stacktrace
        : public std::vector<stacktrace_entry,allocator>
    {
        public:
            using allocator_type = std::vector<stacktrace_entry,allocator>::allocator_type;
            using size_type      = std::vector<stacktrace_entry,allocator>::size_type; 

        public:
            static basic_stacktrace current (                       const allocator_type& = allocator_type() ) noexcept;
            static basic_stacktrace current ( size_type,            const allocator_type& = allocator_type() ) noexcept;
            static basic_stacktrace current ( size_type, size_type, const allocator_type& = allocator_type() ) noexcept;
    };

    template < class allocator > std::ostream& operator << ( std::ostream&, const basic_stacktrace<allocator>& );
    template < class allocator > std::string   to_string   (                const basic_stacktrace<allocator>& );

    using stacktrace = basic_stacktrace<allocator<stacktrace_entry>>;
}



namespace std
{
    constexpr stacktrace_entry::stacktrace_entry ( ) noexcept = default;

    constexpr stacktrace_entry::stacktrace_entry ( const stacktrace_entry& ) noexcept = default;

    constexpr stacktrace_entry::native_handle_type stacktrace_entry::native_handle ( ) const noexcept
    {
        return this->handle;
    }

    constexpr stacktrace_entry::operator bool ( ) const noexcept
    {
        return this->handle != native_handle_type();
    }

    std::string stacktrace_entry::description ( ) const
    {
        return native_stacktrace_entry_description(this->handle);
    }

    std::string stacktrace_entry::source_file ( ) const
    {
        return native_stacktrace_entry_source_file(this->handle);
    }

    std::uint_least32_t stacktrace_entry::source_line ( ) const
    {
        return native_stacktrace_entry_source_line(this->handle);
    }

    constexpr stacktrace_entry::stacktrace_entry ( native_handle_type init_handle ) noexcept
        : handle(init_handle)
    {

    }

    constexpr bool operator == ( const stacktrace_entry& left, const stacktrace_entry& right ) noexcept
    {
        return left.native_handle() == right.native_handle();
    }

    constexpr std::strong_ordering operator <=> ( const stacktrace_entry& left, const stacktrace_entry& right ) noexcept
    {
        return left.native_handle() <=> right.native_handle();
    }

    std::ostream& operator << ( std::ostream& left, const stacktrace_entry& right )
    {
        return left << right.description();
    }

    std::string to_string ( const stacktrace_entry& entry )
    {
        return entry.description();
    } 

    template < class allocator >
    basic_stacktrace<allocator> basic_stacktrace<allocator>::current ( const allocator_type& alloc ) noexcept
    {
        return basic_stacktrace::current(0, 65536, alloc);
    }

    template < class allocator >
    basic_stacktrace<allocator> basic_stacktrace<allocator>::current ( size_type skip, const allocator_type& alloc ) noexcept
    {
        return basic_stacktrace::current(skip, 65536, alloc);
    }

    template < class allocator >
    basic_stacktrace<allocator> basic_stacktrace<allocator>::current ( size_type skip, size_type max_depth, const allocator_type& alloc ) noexcept
    {
        auto trace = basic_stacktrace<allocator>();
        std::ranges::copy(native_stacktrace_current() | std::views::drop(skip) | std::views::take(max_depth - skip), std::back_inserter(trace));
        return trace;
    }

    template < class allocator >
    std::ostream& operator << ( std::ostream& left, const basic_stacktrace<allocator>& right )
    {
        for (const auto& entry : right)
            left << entry << '\n';
        return left;
    }

    template < class allocator >
    std::string to_string ( const basic_stacktrace<allocator>& trace )
    {
        auto string = std::string();
        for (const auto& entry : trace)
            string += (to_string(entry) + '\n');
        return string;
    }
}
