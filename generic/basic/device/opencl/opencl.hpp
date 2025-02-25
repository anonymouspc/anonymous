#pragma once

#include "execution/opencl_queue_context.hpp"
#include "execution/opencl_queue_scope.hpp"

class opencl
{
    public: // Execution
        using  execution_context_type = detail::opencl_queue_context;
        static execution_context_type execution_context;

    public: // Type
        template < class type > using value_type = type;
        template < class type > class reference;
        template < class type > class const_reference;
        template < class type > class pointer;
        template < class type > class const_pointer;
        template < class type > class stride_pointer;
        template < class type > class const_stride_pointer;

    public: // Allocator
        template < class type > using allocator = boost::compute::buffer_allocator<type>;

    public: // Memory
                                using layout_type         = std::layout_left;
        template < class type > class accessor_type;

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

    public: // Hash
        template < class type > using hash = boost::compute::hash<type>;

    public: // Container
        template < class type, int len >                                                                                                                      class array;
        template < class type, class traits = std::char_traits<type>, class alloc = allocator<type> >                                                         class basic_string;     
        template < class type, class traits = std::char_traits<type> >                                                                                        class basic_string_view;
     // template < class type, class alloc = allocator<type> >                                                                                                using deque              = unsupported;
     // template < class type, int len >                                                                                                                      using inplace_vector     = unsupported;
     // template < class type, class alloc = allocator<type> >                                                                                                using list               = unsupported;
     // template < class type1, class type2, class compare = less<type1>, class alloc = allocator<std::pair<const type1,type2>> >                             using map                = supported, but too many bugs.
     // template < class type, class compare = less<type>, class alloc = allocator<type> >                                                                    using priority_queue     = unsupported;
     // template < class type, class alloc = allocator<type> >                                                                                                using queue              = unsupported;
        template < class type, class compare = less<type>, class alloc = allocator<type> >                                                                    class set;
        template < class type, class alloc = allocator<type> >                                                                                                class stack;         
     // template < class type1, class type2, class hash = hash<type1>, class equal = equal_to<type1>, class alloc = allocator<std::pair<const type1,type2>> > using unordered_map      = unsupported;
     // template < class type, class hash = hash<type>, class equal = equal_to<type>,  class alloc = allocator<type> >                                        using unordered_set      = unsupported;
        template < class type, class alloc = allocator<type> >                                                                                                class vector;

    public: // Algorithm
        static decltype(auto) accumulate                        ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::accumulate              (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) adjacent_difference               ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::adjacent_difference     (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) adjacent_find                     ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::adjacent_find           (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) all_of                            ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::all_of                  (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) any_of                            ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::any_of                  (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) binary_search                     ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::binary_search           (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) copy                              ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::copy                    (std::forward<decltype(args)>(args)..., scope.command_queue()); }
     // static decltype(auto) copy_backward                     ( auto&&... args ) { unsupported }
        static decltype(auto) copy_if                           ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::copy_if                 (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) copy_n                            ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::copy_n                  (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) count                             ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::count                   (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) count_if                          ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::count_if                (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) equal                             ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::equal                   (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) equal_range                       ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::equal_range             (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) exclusive_scan                    ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::exclusive_scan          (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) fill                              ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::fill                    (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) fill_n                            ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::fill_n                  (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) find                              ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::find                    (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) find_end                          ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::find_end                (std::forward<decltype(args)>(args)..., scope.command_queue()); }
     // static decltype(auto) find_first_of                     ( auto&&... args ) { unsupported }
        static decltype(auto) find_if                           ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::find_if                 (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) find_if_not                       ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::find_if_not             (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) for_each                          ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::for_each                (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) for_each_n                        ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::for_each_n              (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) generate                          ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::generate                (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) generate_n                        ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::generate_n              (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) includes                          ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::includes                (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) inclusive_scan                    ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::inclusive_scan          (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) inner_product                     ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::inner_product           (std::forward<decltype(args)>(args)..., scope.command_queue()); }
     // static decltype(auto) inplace_merge                     ( auto&&... args ) { unsupported }
        static decltype(auto) iota                              ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::iota                    (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) is_partitioned                    ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::is_partitioned          (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) is_permutation                    ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::is_permutation          (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) is_sorted                         ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::is_sorted               (std::forward<decltype(args)>(args)..., scope.command_queue()); }
     // static decltype(auto) is_sorted_until                   ( auto&&... args ) { unsupported }
        static decltype(auto) lower_bound                       ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::lower_bound             (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) lexicographical_compare           ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::lexicographical_compare (std::forward<decltype(args)>(args)..., scope.command_queue()); }
     // static decltype(auto) lexicographical_compare_three_way ( auto&&... args ) { unsupported }
        static decltype(auto) max_element                       ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::max_element             (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) merge                             ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::merge                   (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) min_element                       ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::min_element             (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) minmax_element                    ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::minmax_element          (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) mismatch                          ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::mismatch                (std::forward<decltype(args)>(args)..., scope.command_queue()); }
  /*!*/ static decltype(auto) move                              ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::copy                    (std::forward<decltype(args)>(args)..., scope.command_queue()); }
     // static decltype(auto) move_backward                     ( auto&&... args ) { unsupported }
        static decltype(auto) next_permutation                  ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::next_permutation        (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) none_of                           ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::none_of                 (std::forward<decltype(args)>(args)..., scope.command_queue()); }
     // static decltype(auto) nth_element                       ( auto&&... args ) { unsupported }
     // static decltype(auto) partial_sort                      ( auto&&... args ) { unsupported }
     // static decltype(auto) partial_sort_copy                 ( auto&&... args ) { unsupported }
        static decltype(auto) partial_sum                       ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::partial_sum             (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) partition                         ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::partition               (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) partition_copy                    ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::partition_copy          (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) partition_point                   ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::partition_point         (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) prev_permutation                  ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::prev_permutation        (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) reduce                            ( auto&&... args ); 
        static decltype(auto) remove                            ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::remove                  (std::forward<decltype(args)>(args)..., scope.command_queue()); }
     // static decltype(auto) remove_copy                       ( auto&&... args ) { unsupported }
     // static decltype(auto) remove_copy_if                    ( auto&&... args ) { unsupported }
        static decltype(auto) remove_if                         ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::remove_if               (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) replace                           ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::replace                 (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) replace_copy                      ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::replace_copy            (std::forward<decltype(args)>(args)..., scope.command_queue()); }
     // static decltype(auto) replace_copy_if                   ( auto&&... args ) { unsupported }
     // static decltype(auto) replace_if                        ( auto&&... args ) { unsupported }
        static decltype(auto) reverse                           ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::reverse                 (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) reverse_copy                      ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::reverse_copy            (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) rotate                            ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::rotate                  (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) rotate_copy                       ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::rotate_copy             (std::forward<decltype(args)>(args)..., scope.command_queue()); }
     // static decltype(auto) sample                            ( auto&&... args ) { unsupported }
        static decltype(auto) search                            ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::search                  (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) search_n                          ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::search_n                (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) set_difference                    ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::set_difference          (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) set_intersection                  ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::set_intersection        (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) set_symmetric_difference          ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::set_symmetric_difference(std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) set_union                         ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::set_union               (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) shift_left                        ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::shift_left              (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) shift_right                       ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::shift_right             (std::forward<decltype(args)>(args)..., scope.command_queue()); }
     // static decltype(auto) shuffle                           ( auto&&... args ) { unsupported }
        static decltype(auto) sort                              ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::sort                    (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) stable_partition                  ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::stable_partition        (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) stable_sort                       ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::stable_sort             (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) swap_ranges                       ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::swap_ranges             (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) transform                         ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::transform               (std::forward<decltype(args)>(args)..., scope.command_queue()); }
     // static decltype(auto) transform_exclusive_scan          ( auto&&... args ) { unsupported }
     // static decltype(auto) transform_inclusive_scan          ( auto&&... args ) { unsupported }
        static decltype(auto) transform_reduce                  ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::transform_reduce        (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) unique                            ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::unique                  (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) unique_copy                       ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::unique_copy             (std::forward<decltype(args)>(args)..., scope.command_queue()); }
        static decltype(auto) upper_bound                       ( auto&&... args ) { let scope = detail::opencl_queue_scope(); return boost::compute::upper_bound             (std::forward<decltype(args)>(args)..., scope.command_queue()); }

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
};

#include "type/reference.hpp"
#include "type/pointer.hpp"
#include "type/stride_pointer.hpp"
#include "type/type_traits.hpp"

#include "operator/operator.hpp"
#include "operator/type_traits.hpp"

#include "memory/accessor_type.hpp"

#include "container/array.hpp"
#include "container/basic_string.hpp"
#include "container/basic_string_view.hpp"
#include "container/set.hpp"
#include "container/stack.hpp"
#include "container/vector.hpp"

#include "algorithm/reduce.hpp"

//#include "linalg/linalg.hpp"

opencl::execution_context_type opencl::execution_context = opencl::execution_context_type(boost::compute::system::default_device().max_work_group_size());

