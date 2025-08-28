export module anonymous:basic.concepts.ios;
import                 :basic.concepts.core;
import                 :basic.concepts.numbers;
import        std;

export namespace anonymous
{
    template < class type > concept sync_reader  = requires ( type& r, char* c, int s ) { { r.read       (c, s) } -> convertible_to<int>; };
    template < class type > concept sync_writer  = requires ( type& r, char* c, int s ) { { r.write      (c, s) } -> convertible_to<int>; };
    template < class type > concept async_reader = requires ( type& r, char* c, int s ) { { r.async_read (c, s) } -> std::execution::sender; };
    template < class type > concept async_writer = requires ( type& r, char* c, int s ) { { r.async_write(c, s) } -> std::execution::sender; };
    template < class type > concept reader       = sync_reader<type> and async_reader<type>;
    template < class type > concept writer       = sync_writer<type> and async_writer<type>;
}