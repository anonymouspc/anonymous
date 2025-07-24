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
         //                                                                                           using any             = unsupported;
         // template < class type, int len >                                                          using array           = unsupported;
         // template < class type, class traits = char_traits<type> >                                 using basic_string    = unsupported;
         // template < int len >                                                                      using bitset          = unsupported;
         // template < class type >                                                                   using deque           = unsupported;
         // template < class type, class error >                                                      using expected        = unsupported;
         // template < class type >                                                                   using forward_list    = unsupported;
         // template < class type >                                                                   using function        = unsupported;
         // template < class type >                                                                   using hive            = unsupported;
         // template < class type, int len >                                                          using inplace_vector  = unsupported;
         // template < class type >                                                                   using list            = unsupported;
            template < class type1, class type2, class compare = less<> >                             using map             = ::tbb::concurrent_map          <type1,type2,compare>;
         // template < class type >                                                                   using optional        = unsupported;
            template < class type, class compare = less<> >                                           class priority_queue; // Override pop().
            template < class type >                                                                   class queue;          // Override pop()
            template < class type, class compare = less<> >                                           using set             = ::tbb::concurrent_set          <type,compare>;
         // template < class type >                                                                   using stack           = unsupported;
            template < class type1, class type2, class hash = hash<type1>, class equal = equal_to<> > using unordered_map   = ::tbb::concurrent_unordered_map<type1,type2,hash,equal>;
            template < class type, class hash = hash<type>, class equal = equal_to<> >                using unordered_set   = ::tbb::concurrent_unordered_set<type,hash,equal>;
         // template < class type >                                                                   using valarray        = unsupported;
         // template < class... types >                                                               using variant         = unsupported;
         // template < class type >                                                                   using vector          = supported, but does not satisfy std::contiguous_range.
    };
}