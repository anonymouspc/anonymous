export module anonymous:basic.device.cpu.decl.cpu;
import                 :basic.concepts;
import        std;
import        exec;

export namespace anonymous
{
    class cpu
    {
        public: // Execution
            using execution_context_type = exec::static_thread_pool;
            inline static execution_context_type execution_context = execution_context_type(std::thread::hardware_concurrency());

        public: // Type
            template < class type > using value_type      =       type;
            template < class type > using reference       =       type&;
            template < class type > using const_reference = const type&;
            template < class type > using pointer         =       type*;
            template < class type > using const_pointer   = const type*;

        public: // Operator
            template < class type = void > using plus          = std::plus         <type>;
            template < class type = void > using minus         = std::minus        <type>;
            template < class type = void > using multiplies    = std::multiplies   <type>;
            template < class type = void > using divides       = std::divides      <type>;
            template < class type = void > using modulus       = std::modulus      <type>;
            template < class type = void > using negate        = std::negate       <type>;
            template < class type = void > using equal_to      = std::equal_to     <type>;
            template < class type = void > using not_equal_to  = std::not_equal_to <type>;
            template < class type = void > using less          = std::less         <type>;
            template < class type = void > using less_equal    = std::less_equal   <type>;
            template < class type = void > using greater       = std::greater      <type>;
            template < class type = void > using greater_equal = std::greater_equal<type>; 
            template < class type = void > using logical_and   = std::logical_and  <type>;
            template < class type = void > using logical_or    = std::logical_or   <type>;
            template < class type = void > using logical_not   = std::logical_not  <type>;
            template < class type = void > using bit_and       = std::bit_and      <type>;
            template < class type = void > using bit_or        = std::bit_or       <type>;
            template < class type = void > using bit_xor       = std::bit_xor      <type>;
            template < class type = void > using bit_not       = std::bit_not      <type>;

        public: // Cast
            template < class type > class explicit_cast;
            template < class type > class implicit_cast;

        public: // Allocator
            template < class type > using allocator = std::allocator<type>;

        public: // Layout
                                      using default_layout   = std::layout_right;
                                      using layout_right     = std::layout_right;
                                      using layout_left      = std::layout_left;
                                      using layout_stride    = std::layout_stride;
            template < class layout > using layout_transpose = std::linalg::layout_transpose<layout>;

        public: // Accessor
            template < class type >                  using default_accessor    = std::default_accessor           <type>;
            template < class type, size_t align >    using aligned_accessor    = std::aligned_accessor           <type,align>;
            template < class scale, class accessor > using scaled_accessor     = std::linalg::scaled_accessor    <scale,accessor>;
            template < class accessor >              using conjugated_accessor = std::linalg::conjugated_accessor<accessor>;

        public: // Hash
            template < class type = void > using hash = std::hash<type>;

        public: // Structure
            template < class type1, class type2 > using pair  = std::pair <type1,type2>;
            template < class... types >           using tuple = std::tuple<types...>;

        public: // Container
                                                                                                      using any            = std::any;
            template < class type, int len >                                                          using array          = std::array            <type,len>;
            template < class type, class traits = std::char_traits<type> >                            using basic_string   = std::basic_string     <type,traits>;
            template < int len >                                                                      using bitset         = std::bitset           <len>;
            template < class type >                                                                   using deque          = std::deque            <type>;
            template < class type, class error >                                                      using expected       = std::expected         <type,error>;
            template < class type >                                                                   using forward_list   = std::forward_list     <type>;
            template < class type >                                                                   using function       = std::function         <type>;
            template < class type >                                                                   using hive           = std::hive             <type>;
            template < class type, int len >                                                          using inplace_vector = std::inplace_vector   <type,len>;
            template < class type >                                                                   using list           = std::list             <type>;
            template < class type1, class type2, class compare = less<> >                             using map            = std::map              <type1,type2,compare>;
            template < class type >                                                                   using optional       = std::optional         <type>;
            template < class type, class compare = less<> >                                           using priority_queue = std::priority_queue   <type,std::vector<type>,compare>;
            template < class type >                                                                   using queue          = std::queue            <type,std::vector<type>>;
            template < class type, class compare = less<> >                                           using set            = std::set              <type,compare>;
            template < class type >                                                                   using stack          = std::stack            <type,std::vector<type>>;
            template < class type1, class type2, class hash = hash<type1>, class equal = equal_to<> > using unordered_map  = std::unordered_map    <type1,type2,hash,equal>;
            template < class type, class hash = hash<type>, class equal = equal_to<> >                using unordered_set  = std::unordered_set    <type,hash,equal>;
            template < class type >                                                                   using valarray       = std::valarray         <type>;
            template < class... types >                                                               using variant        = std::variant          <types...>;
            template < class type >                                                                   using vector         = std::vector           <type>;

        public: // Span
            template < class type, size_t extent >                                                                         using span   = std::span  <type,extent>;
            template < class type, class extents, class layout = default_layout, class accessor = default_accessor<type> > using mdspan = std::mdspan<type,extents,layout,accessor>;

        public: // Iterator
            template < class iterator >                 using const_iterator   = std::const_iterator  <iterator>;
            template < class iterator >                 using move_iterator    = std::move_iterator   <iterator>;
            template < class iterator >                 using counted_iterator = std::counted_iterator<iterator>;
            template < class iterator >                 using reverse_iterator = std::reverse_iterator<iterator>;
            template < class iterator >                 class stride_iterator;
            template < class iterator, class function > class transform_iterator;

        public: // Algorithm
            static constexpr decltype(auto) accumulate                        ( auto&&... args ) { return std::accumulate                       (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) adjacent_difference               ( auto&&... args ) { return std::adjacent_difference              (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) adjacent_find                     ( auto&&... args ) { return std::adjacent_find                    (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) all_of                            ( auto&&... args ) { return std::all_of                           (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) any_of                            ( auto&&... args ) { return std::any_of                           (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) binary_search                     ( auto&&... args ) { return std::binary_search                    (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) copy                              ( auto&&... args ) { return std::copy                             (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) copy_backward                     ( auto&&... args ) { return std::copy_backward                    (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) copy_if                           ( auto&&... args ) { return std::copy_if                          (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) copy_n                            ( auto&&... args ) { return std::copy_n                           (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) count                             ( auto&&... args ) { return std::count                            (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) count_if                          ( auto&&... args ) { return std::count_if                         (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) equal                             ( auto&&... args ) { return std::equal                            (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) equal_range                       ( auto&&... args ) { return std::equal_range                      (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) exclusive_scan                    ( auto&&... args ) { return std::exclusive_scan                   (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) fill                              ( auto&&... args ) { return std::fill                             (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) fill_n                            ( auto&&... args ) { return std::fill_n                           (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) find                              ( auto&&... args ) { return std::find                             (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) find_end                          ( auto&&... args ) { return std::find_end                         (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) find_first_of                     ( auto&&... args ) { return std::find_first_of                    (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) find_if                           ( auto&&... args ) { return std::find_if                          (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) find_if_not                       ( auto&&... args ) { return std::find_if_not                      (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) for_each                          ( auto&&... args ) { return std::for_each                         (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) for_each_n                        ( auto&&... args ) { return std::for_each_n                       (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) generate                          ( auto&&... args ) { return std::generate                         (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) generate_n                        ( auto&&... args ) { return std::generate_n                       (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) includes                          ( auto&&... args ) { return std::includes                         (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) inclusive_scan                    ( auto&&... args ) { return std::inclusive_scan                   (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) inner_product                     ( auto&&... args ) { return std::inner_product                    (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) inplace_merge                     ( auto&&... args ) { return std::inplace_merge                    (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) iota                              ( auto&&... args ) { return std::iota                             (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) is_partitioned                    ( auto&&... args ) { return std::is_partitioned                   (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) is_permutation                    ( auto&&... args ) { return std::is_permutation                   (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) is_sorted                         ( auto&&... args ) { return std::is_sorted                        (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) is_sorted_until                   ( auto&&... args ) { return std::is_sorted_until                  (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) lower_bound                       ( auto&&... args ) { return std::lower_bound                      (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) lexicographical_compare           ( auto&&... args ) { return std::lexicographical_compare          (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) lexicographical_compare_three_way ( auto&&... args ) { return std::lexicographical_compare_three_way(std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) max_element                       ( auto&&... args ) { return std::max_element                      (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) merge                             ( auto&&... args ) { return std::merge                            (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) min_element                       ( auto&&... args ) { return std::min_element                      (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) minmax_element                    ( auto&&... args ) { return std::minmax_element                   (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) mismatch                          ( auto&&... args ) { return std::mismatch                         (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) move                              ( auto&&... args ) { return std::move                             (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) move_backward                     ( auto&&... args ) { return std::move_backward                    (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) next_permutation                  ( auto&&... args ) { return std::next_permutation                 (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) none_of                           ( auto&&... args ) { return std::none_of                          (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) nth_element                       ( auto&&... args ) { return std::nth_element                      (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) partial_sort                      ( auto&&... args ) { return std::partial_sort                     (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) partial_sort_copy                 ( auto&&... args ) { return std::partial_sort_copy                (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) partial_sum                       ( auto&&... args ) { return std::partial_sum                      (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) partition                         ( auto&&... args ) { return std::partition                        (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) partition_copy                    ( auto&&... args ) { return std::partition_copy                   (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) partition_point                   ( auto&&... args ) { return std::partition_point                  (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) prev_permutation                  ( auto&&... args ) { return std::prev_permutation                 (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) reduce                            ( auto&&... args ) { return std::reduce                           (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) remove                            ( auto&&... args ) { return std::remove                           (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) remove_copy                       ( auto&&... args ) { return std::remove_copy                      (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) remove_copy_if                    ( auto&&... args ) { return std::remove_copy_if                   (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) remove_if                         ( auto&&... args ) { return std::remove_if                        (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) replace                           ( auto&&... args ) { return std::replace                          (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) replace_copy                      ( auto&&... args ) { return std::replace_copy                     (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) replace_copy_if                   ( auto&&... args ) { return std::replace_copy_if                  (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) replace_if                        ( auto&&... args ) { return std::replace_if                       (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) reverse                           ( auto&&... args ) { return std::reverse                          (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) reverse_copy                      ( auto&&... args ) { return std::reverse_copy                     (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) rotate                            ( auto&&... args ) { return std::rotate                           (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) rotate_copy                       ( auto&&... args ) { return std::rotate_copy                      (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) sample                            ( auto&&... args ) { return std::sample                           (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) search                            ( auto&&... args ) { return std::search                           (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) search_n                          ( auto&&... args ) { return std::search_n                         (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) set_difference                    ( auto&&... args ) { return std::set_difference                   (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) set_intersection                  ( auto&&... args ) { return std::set_intersection                 (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) set_symmetric_difference          ( auto&&... args ) { return std::set_symmetric_difference         (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) set_union                         ( auto&&... args ) { return std::set_union                        (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) shift_left                        ( auto&&... args ) { return std::shift_left                       (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) shift_right                       ( auto&&... args ) { return std::shift_right                      (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) shuffle                           ( auto&&... args ) { return std::shuffle                          (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) sort                              ( auto&&... args ) { return std::sort                             (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) stable_partition                  ( auto&&... args ) { return std::stable_partition                 (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) stable_sort                       ( auto&&... args ) { return std::stable_sort                      (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) swap_ranges                       ( auto&&... args ) { return std::swap_ranges                      (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) transform                         ( auto&&... args ) { return std::transform                        (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) transform_exclusive_scan          ( auto&&... args ) { return std::transform_exclusive_scan         (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) transform_inclusive_scan          ( auto&&... args ) { return std::transform_inclusive_scan         (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) transform_reduce                  ( auto&&... args ) { return std::transform_reduce                 (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) unique                            ( auto&&... args ) { return std::unique                           (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) unique_copy                       ( auto&&... args ) { return std::unique_copy                      (std::forward<decltype(args)>(args)...); }
            static constexpr decltype(auto) upper_bound                       ( auto&&... args ) { return std::upper_bound                      (std::forward<decltype(args)>(args)...); }

        public: // Linalg
            struct linalg
            {
                static constexpr void unary_plus        ( const auto,             auto );
                static constexpr void unary_minus       ( const auto,             auto );
                static constexpr void plus              ( const auto, const auto, auto );
                static constexpr void minus             ( const auto, const auto, auto );
                static constexpr void left_scale        ( const auto, const auto, auto );
                static constexpr void right_scale       ( const auto, const auto, auto );
                static constexpr void multiply          ( const auto, const auto, auto );
                static constexpr void divide            ( const auto, const auto, auto );
                static constexpr void plus_equal        (       auto, const auto );
                static constexpr void minus_equal       (       auto, const auto );
                static constexpr void right_scale_equal (       auto, const auto );
                static constexpr void multiply_equal    (       auto, const auto );
                static constexpr void divide_equal      (       auto, const auto );

                static constexpr void convolve          ( const auto, const auto, auto );
                static constexpr void cross             ( const auto, const auto, auto );
                static constexpr void dot               ( const auto, const auto, auto );
                static constexpr void fft               ( const auto,             auto );
                static constexpr void ifft              ( const auto,             auto );
                static constexpr void tensor            ( const auto, const auto, auto );

                static constexpr void det               ( const auto,             auto );
                static constexpr void eigen             ( const auto,             auto, auto );
                static constexpr void eigen_value       ( const auto,             auto );
                static constexpr void eigen_vector      ( const auto,             auto );
                static constexpr void evd               ( const auto,             auto, auto, auto );
                static constexpr void inverse           ( const auto,             auto );
                static constexpr void lu                ( const auto,             auto, auto, auto );
                static constexpr void qr                ( const auto,             auto, auto );
                static constexpr void rank              ( const auto,             auto );
                static constexpr void singular          ( const auto,             auto, auto, auto );
                static constexpr void singular_value    ( const auto,             auto );
                static constexpr void singular_vector   ( const auto,             auto, auto );
                static constexpr void svd               ( const auto,             auto, auto, auto );
                static constexpr void tr                ( const auto,             auto );

                static constexpr auto transpose         ( const auto,             auto );
                static constexpr auto hermitian         ( const auto,             auto );
            };

        public: // Random
            using random_context_type = std::default_random_engine;
            inline static thread_local random_context_type random_context = random_context_type(std::random_device()());

                                             using bernoulli_distribution          = std::bernoulli_distribution;
            template < integral       type > using binomial_distribution           = std::binomial_distribution          <type>;
            template < floating_point type > using cauchy_distribution             = std::cauchy_distribution            <type>;
            template < floating_point type > using chi_squared_distribution        = std::chi_squared_distribution       <type>;
            template < integral       type > using discrete_distribution           = std::discrete_distribution          <type>;
            template < floating_point type > using exponential_distribution        = std::exponential_distribution       <type>;
            template < floating_point type > using extreme_value_distribution      = std::extreme_value_distribution     <type>;
            template < floating_point type > using fisher_f_distribution           = std::fisher_f_distribution          <type>;
            template < floating_point type > using gamma_distribution              = std::gamma_distribution             <type>;
            template < integral       type > using geometric_distribution          = std::geometric_distribution         <type>;
            template < integral       type > using lognormal_distribution          = std::lognormal_distribution         <type>;
            template < integral       type > using negative_binomial_distribution  = std::negative_binomial_distribution <type>;
            template < integral       type > using normal_distribution             = std::normal_distribution            <type>;
            template < floating_point type > using piecewise_constant_distribution = std::piecewise_constant_distribution<type>;
            template < floating_point type > using piecewise_linear_distribution   = std::piecewise_linear_distribution  <type>;
            template < integral       type > using poisson_distribution            = std::poisson_distribution           <type>;
            template < floating_point type > using student_t_distribution          = std::student_t_distribution         <type>;
            template < integral       type > using uniform_int_distribution        = std::uniform_int_distribution       <type>;
            template < floating_point type > using uniform_real_distribution       = std::uniform_real_distribution      <type>;
            template < floating_point type > using weibull_distribution            = std::weibull_distribution           <type>;
    };
}