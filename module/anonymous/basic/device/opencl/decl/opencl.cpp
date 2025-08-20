export module anonymous:basic.device.opencl.decl.opencl;
import                 :basic.concepts;
import                 :basic.utility;
import        std;
import        boost.compute;

export namespace anonymous
{
    template < static_string name >
    class opencl
    {
        public: // Execution
            class execution_context_type;
            static execution_context_type execution_context;

        public: // Type
            template < class type > using value_type = type;
            template < class type > class reference;
            template < class type > class const_reference;
            template < class type > class pointer;
            template < class type > class const_pointer;
            template < class type > class stride_pointer;
            template < class type > class const_stride_pointer;

        public: // Operator
            template < class type = void > class plus;
            template < class type = void > class minus;
            template < class type = void > class multiplies;
            template < class type = void > class divides;
            template < class type = void > class negate;
            template < class type = void > class equal_to;
            template < class type = void > class not_equal_to;
            template < class type = void > class less;
            template < class type = void > class less_equal;
            template < class type = void > class greater;
            template < class type = void > class greater_equal;
            template < class type = void > class logical_and;
            template < class type = void > class logical_or;
            template < class type = void > class logical_not;
            template < class type = void > class bit_and;
            template < class type = void > class bit_or;
            template < class type = void > class bit_xor;
            template < class type = void > class bit_not;

        public: // Cast
            template < class type > class explicit_cast;
            template < class type > class implicit_cast;

        public: // Hash
            template < class type > using hash = boost::compute::hash<type>;

        public: // Allocator
            template < class type > using allocator = boost::compute::buffer_allocator<type>;

        public: // Layout
            using default_layout = std::layout_left;

        public: // Accessor
            template < class type >               class default_accessor;
         // template < class type, size_t align > using aligned_accessor = undefined;

        public: // Structure
         // template < class type1, class type2 > using pair  = undefined;
         // template < class... types >           using tuple = undefined;

        public: // Union
         //                                      using any      = undefined;
         // template < class type, class error > using expected = undefined;
            template < class type >              using function = boost::compute::function<type>;
         // template < class type >              using optional = undefined;
         // template < class... types >          using variant  = undefined;

        public: // Container
            template < class type, int len >                                                          class array;
            template < class type >                                                                   class basic_string;
         // template < int len >                                                                      using bitset         = undefined;
         // template < class type >                                                                   using deque          = undefined;
         // template < class type >                                                                   using forward_list   = undefined;
         // template < class type >                                                                   using hive           = undefined;
         // template < class type, int len >                                                          using inplace_vector = undefined;
         // template < class type >                                                                   using list           = undefined;
            template < class type1, class type2, class compare = less<> >                             class map;
         // template < class type, class compare = less<type> >                                       using priority_queue = undefined;
         // template < class type >                                                                   using queue          = undefined;
            template < class type, class compare = less<> >                                           class set;
            template < class type >                                                                   class stack;
         // template < class type1, class type2, class hash = hash<type1>, class equal = equal_to<> > using unordered_map  = undefined;
         // template < class type, class hash = hash<type>, class equal = equal_to<> >                using unordered_set  = undefined;
            template < class type >                                                                   class valarray;
            template < class type >                                                                   class vector;

        public: // Span
            template < class type, size_t extent >                                                                         using span   = std::span  <type,extent>;
            template < class type, class extents, class layout = default_layout, class accessor = default_accessor<type> > using mdspan = std::mdspan<type,extents,layout,accessor>;
        
        public: // Iterator
         // template < class iterator >                 using const_iterator   = undefined;
         // template < class iterator >                 using move_iterator    = undefined;
         // template < class iterator >                 using counted_iterator = undefined;
         // template < class iterator >                 using reverse_iterator = undefined;
            template < class iterator >                 class stride_iterator;
            template < class iterator, class function > class transform_iterator;

        public: // Algorithm
            static decltype(auto) accumulate                        ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::accumulate              (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) adjacent_difference               ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::adjacent_difference     (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) adjacent_find                     ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::adjacent_find           (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) all_of                            ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::all_of                  (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) any_of                            ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::any_of                  (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) binary_search                     ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::binary_search           (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) copy                              ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::copy                    (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
         // static decltype(auto) copy_backward                     ( auto&&... args ) { undefined }
            static decltype(auto) copy_if                           ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::copy_if                 (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) copy_n                            ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::copy_n                  (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) count                             ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::count                   (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) count_if                          ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::count_if                (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) equal                             ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::equal                   (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) equal_range                       ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::equal_range             (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) exclusive_scan                    ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::exclusive_scan          (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) fill                              ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::fill                    (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) fill_n                            ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::fill_n                  (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) find                              ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::find                    (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) find_end                          ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::find_end                (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
         // static decltype(auto) find_first_of                     ( auto&&... args ) { undefined }
            static decltype(auto) find_if                           ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::find_if                 (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) find_if_not                       ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::find_if_not             (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) for_each                          ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::for_each                (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) for_each_n                        ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::for_each_n              (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) generate                          ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::generate                (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) generate_n                        ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::generate_n              (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) includes                          ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::includes                (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) inclusive_scan                    ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::inclusive_scan          (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) inner_product                     ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::inner_product           (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
         // static decltype(auto) inplace_merge                     ( auto&&... args ) { undefined }
            static decltype(auto) iota                              ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::iota                    (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) is_partitioned                    ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::is_partitioned          (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) is_permutation                    ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::is_permutation          (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) is_sorted                         ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::is_sorted               (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
         // static decltype(auto) is_sorted_until                   ( auto&&... args ) { undefined }
            static decltype(auto) lower_bound                       ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::lower_bound             (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) lexicographical_compare           ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::lexicographical_compare (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
         // static decltype(auto) lexicographical_compare_three_way ( auto&&... args ) { undefined }
            static decltype(auto) max_element                       ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::max_element             (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) merge                             ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::merge                   (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) min_element                       ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::min_element             (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) minmax_element                    ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::minmax_element          (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) mismatch                          ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::mismatch                (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
      /*!*/ static decltype(auto) move                              ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::copy                    (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
         // static decltype(auto) move_backward                     ( auto&&... args ) { undefined }
            static decltype(auto) next_permutation                  ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::next_permutation        (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) none_of                           ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::none_of                 (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
         // static decltype(auto) nth_element                       ( auto&&... args ) { undefined }
         // static decltype(auto) partial_sort                      ( auto&&... args ) { undefined }
         // static decltype(auto) partial_sort_copy                 ( auto&&... args ) { undefined }
            static decltype(auto) partial_sum                       ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::partial_sum             (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) partition                         ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::partition               (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) partition_copy                    ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::partition_copy          (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) partition_point                   ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::partition_point         (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) prev_permutation                  ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::prev_permutation        (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) reduce                            ( auto&&... args ); 
            static decltype(auto) remove                            ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::remove                  (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
         // static decltype(auto) remove_copy                       ( auto&&... args ) { undefined }
         // static decltype(auto) remove_copy_if                    ( auto&&... args ) { undefined }
            static decltype(auto) remove_if                         ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::remove_if               (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) replace                           ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::replace                 (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) replace_copy                      ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::replace_copy            (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
         // static decltype(auto) replace_copy_if                   ( auto&&... args ) { undefined }
         // static decltype(auto) replace_if                        ( auto&&... args ) { undefined }
            static decltype(auto) reverse                           ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::reverse                 (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) reverse_copy                      ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::reverse_copy            (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) rotate                            ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::rotate                  (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) rotate_copy                       ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::rotate_copy             (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
         // static decltype(auto) sample                            ( auto&&... args ) { undefined }
            static decltype(auto) search                            ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::search                  (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) search_n                          ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::search_n                (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) set_difference                    ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::set_difference          (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) set_intersection                  ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::set_intersection        (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) set_symmetric_difference          ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::set_symmetric_difference(std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) set_union                         ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::set_union               (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) shift_left                        ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::shift_left              (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) shift_right                       ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::shift_right             (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
         // static decltype(auto) shuffle                           ( auto&&... args ) { undefined }
            static decltype(auto) sort                              ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::sort                    (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) stable_partition                  ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::stable_partition        (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) stable_sort                       ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::stable_sort             (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) swap_ranges                       ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::swap_ranges             (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) transform                         ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::transform               (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
         // static decltype(auto) transform_exclusive_scan          ( auto&&... args ) { undefined }
         // static decltype(auto) transform_inclusive_scan          ( auto&&... args ) { undefined }
            static decltype(auto) transform_reduce                  ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::transform_reduce        (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) unique                            ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::unique                  (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) unique_copy                       ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::unique_copy             (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }
            static decltype(auto) upper_bound                       ( auto&&... args ) { auto que = std::unique_ptr(nullptr, [] (auto) { execution_context.command_queue().finish(); }); return boost::compute::upper_bound             (std::forward<decltype(args)>(args)..., execution_context.command_queue()); }

        public: // Linalg
            struct linalg
            {
                constexpr static void unary_plus        ( const auto,             auto );
                constexpr static void unary_minus       ( const auto,             auto );
                constexpr static void plus              ( const auto, const auto, auto );
                constexpr static void minus             ( const auto, const auto, auto );
                constexpr static void left_scale        ( const auto, const auto, auto );
                constexpr static void right_scale       ( const auto, const auto, auto );
                constexpr static void multiply          ( const auto, const auto, auto );
                constexpr static void divide            ( const auto, const auto, auto );
                constexpr static void plus_equal        (       auto, const auto, auto );
                constexpr static void minus_equal       (       auto, const auto, auto );
                constexpr static void right_scale_equal (       auto, const auto, auto );
                constexpr static void multiply_equal    (       auto, const auto, auto );
                constexpr static void divide_equal      (       auto, const auto, auto );

                constexpr static void convolve          ( const auto, const auto, auto );
                constexpr static void cross             ( const auto, const auto, auto );
                constexpr static void dot               ( const auto, const auto, auto );
                constexpr static void fft               ( const auto,             auto );
                constexpr static void ifft              ( const auto,             auto );
                constexpr static void tensor            ( const auto, const auto, auto );

                constexpr static void det               ( const auto,             auto );
                constexpr static void eigen             ( const auto,             auto, auto );
                constexpr static void eigen_value       ( const auto,             auto );
                constexpr static void eigen_vector      ( const auto,             auto );
                constexpr static void evd               ( const auto,             auto, auto, auto );
                constexpr static void inverse           ( const auto,             auto );
                constexpr static void lu                ( const auto,             auto, auto, auto );
                constexpr static void qr                ( const auto,             auto, auto );
                constexpr static void rank              ( const auto,             auto );
                constexpr static void singular          ( const auto,             auto, auto, auto );
                constexpr static void singular_value    ( const auto,             auto );
                constexpr static void singular_vector   ( const auto,             auto, auto );
                constexpr static void svd               ( const auto,             auto, auto, auto );
                constexpr static void tr                ( const auto,             auto );

                constexpr static auto transpose         ( const auto,             auto );
                constexpr static auto hermitian         ( const auto,             auto );
            };

        public: // Random
            class random_context_type;
            static thread_local random_context_type random_context;

                                             using bernoulli_distribution          = boost::compute::bernoulli_distribution   <>;
         // template < integral       type > using binomial_distribution           = undefined;
         // template < floating_point type > using cauchy_distribution             = undefined;
         // template < floating_point type > using chi_squared_distribution        = undefined;
            template < integral       type > using discrete_distribution           = boost::compute::discrete_distribution    <type>;
         // template < floating_point type > using exponential_distribution        = undefined;
         // template < floating_point type > using extreme_value_distribution      = undefined;
         // template < floating_point type > using fisher_f_distribution           = undefined;
         // template < floating_point type > using gamma_distribution              = undefined;
         // template < integral       type > using geometric_distribution          = undefined;
         // template < integral       type > using lognormal_distribution          = undefined;
         // template < integral       type > using negative_binomial_distribution  = undefined;
            template < integral       type > using normal_distribution             = boost::compute::normal_distribution      <type>;
         // template < floating_point type > using piecewise_constant_distribution = undefined;
         // template < floating_point type > using piecewise_linear_distribution   = undefined;
         // template < integral       type > using poisson_distribution            = undefined;
         // template < floating_point type > using student_t_distribution          = undefined;
            template < integral       type > using uniform_int_distribution        = boost::compute::uniform_int_distribution <type>;
            template < floating_point type > using uniform_real_distribution       = boost::compute::uniform_real_distribution<type>;
         // template < floating_point type > using weibull_distribution            = undefined;
    };

}