export module anonymous:basic.device.tbb.decl.tbb;
import                 :basic.device.cpu;
import        tbb;

export namespace anonymous
{
    class tbb
        extends public cpu
    {
        public: // Allocator
            template < class type > using allocator = ::tbb::tbb_allocator<type>;

        public: // Container
         // template < class type, int len >                                                          using array           = undefined;
         // template < class type, class traits = char_traits<type> >                                 using basic_string    = undefined;
         // template < int len >                                                                      using bitset          = undefined;
         // template < class type >                                                                   using deque           = undefined;
         // template < class type >                                                                   using forward_list    = undefined;
         // template < class type >                                                                   using hive            = undefined;
         // template < class type, int len >                                                          using inplace_vector  = undefined;
         // template < class type >                                                                   using list            = undefined;
            template < class type1, class type2, class compare = less<> >                             using map             = ::tbb::concurrent_map          <type1,type2,compare>;
            template < class type, class compare = less<> >                                           class priority_queue; // Override pop().
            template < class type >                                                                   class queue;          // Override pop()
            template < class type, class compare = less<> >                                           using set             = ::tbb::concurrent_set          <type,compare>;
         // template < class type >                                                                   using stack           = undefined;
            template < class type1, class type2, class hash = hash<type1>, class equal = equal_to<> > using unordered_map   = ::tbb::concurrent_unordered_map<type1,type2,hash,equal>;
            template < class type, class hash = hash<type>, class equal = equal_to<> >                using unordered_set   = ::tbb::concurrent_unordered_set<type,hash,equal>;
         // template < class type >                                                                   using valarray        = undefined;
         // template < class type >                                                                   using vector          = supported, but does not satisfy std::contiguous_range.
    };
}