export module anonymous:basic.device.pmr.decl.pmr;
import                 :basic.device.cpu;
import        std;

export namespace anonymous
{
    class pmr
        extends public cpu
    {
        public: // Allocator
            template < class type > using allocator = std::pmr::polymorphic_allocator<type>;

        public: // Container
         //                                                                                           using any            = unsupported;
         // template < class type, int len >                                                          using array          = unsupported;
            template < class type, class traits = std::char_traits<type> >                            using basic_string   = std::pmr::basic_string     <type,traits>;
         // template < int len >                                                                      using bitset         = unsupported;
            template < class type >                                                                   using deque          = std::pmr::deque            <type>;
         // template < class type, class error >                                                      using expected       = unsupported;
            template < class type >                                                                   using forward_list   = std::pmr::forward_list     <type>;
         // template < class type >                                                                   using function       = unsupported;
            template < class type >                                                                   using hive           = std::pmr::hive             <type>;
         // template < class type, int len >                                                          using inplace_vector = unsupported;
            template < class type >                                                                   using list           = std::pmr::list             <type>;
            template < class type1, class type2, class compare = less<> >                             using map            = std::pmr::map              <type1,type2,compare>;
         // template < class type >                                                                   using optional       = unsupported;
            template < class type, class compare = less<> >                                           using priority_queue = std::     priority_queue   <type,std::pmr::vector<type>,compare>;
            template < class type >                                                                   using queue          = std::     queue            <type,std::pmr::vector<type>>;
            template < class type, class compare = less<> >                                           using set            = std::pmr::set              <type,compare>;
            template < class type >                                                                   using stack          = std::     stack            <type,std::pmr::vector<type>>;
            template < class type1, class type2, class hash = hash<type1>, class equal = equal_to<> > using unordered_map  = std::pmr::unordered_map    <type1,type2,hash,equal>;
            template < class type, class hash = hash<type>, class equal = equal_to<> >                using unordered_set  = std::pmr::unordered_set    <type,hash,equal>;
         // template < class type >                                                                   using valarray       = unsupported;
         // template < class... types >                                                               using variant        = unsupported;
            template < class type >                                                                   using vector         = std::pmr::vector           <type>;
    };
}