module;
#undef in
#undef self
#undef extends
#ifdef __clang__
    #pragma clang diagnostic ignored "-Wdeprecated-missing-comma-variadic-parameter"
#endif
#define BOOST_COMPUTE_USE_CPP11
#include <boost/compute.hpp>
#include <boost/compute/container/stack.hpp>
#include <boost/compute/container/valarray.hpp>

export module boost.compute;
import        std;
import        opencl;

export namespace boost::compute
{
    using boost::compute::array;
    using boost::compute::basic_string;
    using boost::compute::buffer_allocator;
    using boost::compute::command_queue;
    using boost::compute::flat_map;
    using boost::compute::flat_set;
    using boost::compute::hash;
    using boost::compute::stack;
    using boost::compute::system;
    using boost::compute::valarray;
    using boost::compute::vector;

    using boost::compute::function;

    using boost::compute::accumulate;
    using boost::compute::adjacent_difference;
    using boost::compute::adjacent_find;
    using boost::compute::all_of;
    using boost::compute::any_of;
    using boost::compute::binary_search;
    using boost::compute::copy;
    using boost::compute::copy_if;
    using boost::compute::copy_n;
    using boost::compute::count;
    using boost::compute::count_if;
    using boost::compute::equal;
    using boost::compute::equal_range;
    using boost::compute::exclusive_scan;
    using boost::compute::fill;
    using boost::compute::fill_n;
    using boost::compute::find;
    using boost::compute::find_end;
    using boost::compute::find_if;
    using boost::compute::find_if_not;
    using boost::compute::for_each;
    using boost::compute::for_each_n;
    using boost::compute::generate;
    using boost::compute::generate_n;
    using boost::compute::includes;
    using boost::compute::inclusive_scan;
    using boost::compute::inner_product;
    using boost::compute::iota;
    using boost::compute::is_partitioned;
    using boost::compute::is_permutation;
    using boost::compute::is_sorted;
    using boost::compute::lower_bound;
    using boost::compute::lexicographical_compare;
    using boost::compute::max_element;
    using boost::compute::merge;
    using boost::compute::min_element;
    using boost::compute::minmax_element;
    using boost::compute::mismatch;
    using boost::compute::next_permutation;
    using boost::compute::none_of;
    using boost::compute::partial_sum;
    using boost::compute::partition;
    using boost::compute::partition_copy;
    using boost::compute::partition_point;
    using boost::compute::prev_permutation;
    using boost::compute::reduce;
    using boost::compute::remove;
    using boost::compute::remove_if;
    using boost::compute::replace;
    using boost::compute::replace_copy;
    using boost::compute::reverse;
    using boost::compute::reverse_copy;
    using boost::compute::rotate;
    using boost::compute::rotate_copy;
    using boost::compute::search;
    using boost::compute::search_n;
    using boost::compute::set_difference;
    using boost::compute::set_intersection;
    using boost::compute::set_symmetric_difference;
    using boost::compute::set_union;
    using boost::compute::shift_left;
    using boost::compute::shift_right;
    using boost::compute::sort;
    using boost::compute::stable_partition;
    using boost::compute::stable_sort;
    using boost::compute::swap_ranges;
    using boost::compute::transform;
    using boost::compute::transform_reduce;
    using boost::compute::unique;
    using boost::compute::unique_copy;
    using boost::compute::upper_bound;

    using boost::compute::default_random_engine;
    using boost::compute::bernoulli_distribution;
    using boost::compute::discrete_distribution;
    using boost::compute::normal_distribution;
    using boost::compute::uniform_int_distribution;
    using boost::compute::uniform_real_distribution;
}