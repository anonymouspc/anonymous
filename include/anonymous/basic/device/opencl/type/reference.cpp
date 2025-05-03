template < class type >
opencl::template reference<type> opencl::reference<type>::operator = ( const reference& right )
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void assign ( __global type* self_buf, int self_idx, __global type* right_buf, int right_idx )
        {
            self_buf[self_idx] = right_buf[right_idx];
        }
    ), type(), "type");

    auto kernel = opencl::execution_context.build_kernel(program, "assign");
    kernel.set_args(self.get_buffer(), self.get_index(), right.get_buffer(), right.get_index());
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return self;
}

template < class type >
opencl::template reference<type> opencl::reference<type>::operator = ( type right )
{
    boost::compute::detail::write_single_value<type>(right, buf, idx, opencl::execution_context.command_queue());
    opencl::execution_context.command_queue().finish();
    return self;
}

template < class type >
opencl::template reference<type> opencl::reference<type>::operator = ( opencl::template const_reference<type> right )
{
    return self = opencl::template reference<type>(right);
}

template < class type >
template < class type2 >
opencl::template reference<type> opencl::reference<type>::operator = ( type2 right )
    requires convertible_to<type2,type>
{
    return self = type(right);
}

template < class type >
template < class type2 >
opencl::template reference<type> opencl::reference<type>::operator = ( opencl::template reference<type2> right )
    requires convertible_to<type2,type>
{
    using type1 = type;
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void assign ( __global type1* self_buf, int self_idx, __global type2* right_buf, int right_idx )
        {
            self_buf[self_idx] = right_buf[right_idx];
        }
    ), type1(), "type1", type2(), "type2");
    
    auto kernel = opencl::execution_context.build_kernel(program, "assign");
    kernel.set_args(self.get_buffer(), self.get_index(), right.get_buffer(), right.get_index());
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return self;
}

template < class type >
template < class type2 >
opencl::template reference<type> opencl::reference<type>::operator = ( opencl::template const_reference<type2> right )
    requires convertible_to<type2,type>
{
    return self = opencl::template reference<type2>(right);
}

template < class type >
opencl::reference<type>::reference ( opencl::template const_reference<type> cvt )
    extends reference ( cvt.get_buffer(), cvt.get_index() )
{
    
}

template < class type >
opencl::reference<type>::operator type ( ) const
{
    auto cvt = boost::compute::detail::read_single_value<type>(buf, idx, opencl::execution_context.command_queue());
    opencl::execution_context.command_queue().finish();
    return cvt;
}

template < class type >
opencl::reference<type>::reference ( boost::compute::buffer cvt_buf, size_t cvt_idx )
    extends buf ( cvt_buf ),
            idx ( cvt_idx )
{
    
}

template < class type >
opencl::reference<type>::reference ( boost::compute::detail::buffer_value<type> cvt )
    extends reference ( (&cvt).get_buffer(), (&cvt).get_index() / sizeof(type) )
{
    
}

template < class type >
opencl::reference<type>::operator boost::compute::detail::buffer_value<type> ( ) const
{
    return boost::compute::detail::buffer_value<type>(get_buffer(), get_index() * sizeof(type));
}

template < class type >
boost::compute::buffer opencl::reference<type>::get_buffer ( ) const
{
    return buf;
}

template < class type >
size_t opencl::reference<type>::get_index ( ) const
{
    return idx;
}




template < class type >
opencl::const_reference<type>::const_reference ( opencl::template reference<type> cvt )
    extends const_reference ( cvt.get_buffer(), cvt.get_index() )
{
    
}

template < class type >
opencl::const_reference<type>::operator type ( ) const
{
    auto cvt = boost::compute::detail::read_single_value<type>(buf, idx, opencl::execution_context.command_queue());
    opencl::execution_context.command_queue().finish();
    return cvt;
}

template < class type >
opencl::const_reference<type>::const_reference ( boost::compute::buffer cvt_buf, size_t cvt_idx )
    extends buf ( cvt_buf ),
            idx ( cvt_idx )
{
    
}

template < class type >
opencl::const_reference<type>::const_reference ( boost::compute::detail::buffer_value<type> cvt )
    extends const_reference ( (&cvt).get_buffer(), (&cvt).get_index() / sizeof(type) )
{
    
}

template < class type >
const boost::compute::buffer opencl::const_reference<type>::get_buffer ( ) const
{
    return buf;
}

template < class type >
size_t opencl::const_reference<type>::get_index ( ) const
{
    return idx;
}




// Operator

/* operators (+, -, *, /, ...) which accepts one/two
 * device rvalue, and returns a host rvalue, does not need
 * to be declared. They will use built-in operators.
 */

template < class type >
opencl::template pointer<type> operator & ( opencl::template reference<type> right )
{
    return opencl::template pointer<type>(right.get_buffer(), right.get_index());
}

template < class type >
opencl::template const_pointer<type> operator & ( opencl::template const_reference<type> right )
{
    return opencl::template const_pointer<type>(right.get_buffer(), right.get_index());
}

template < class type1, class type2 >
bool operator == ( opencl::template reference<type1> left, opencl::template reference<type2> right )
    requires requires ( type1 a, type2 b ) { a == b; }
{
    return opencl::template const_reference<type1>(left) == opencl::template const_reference<type2>(right);
}

template < class type1, class type2 >
bool operator == ( opencl::template reference<type1> left, opencl::template const_reference<type2> right )
    requires requires ( type1 a, type2 b ) { a == b; }
{
    return opencl::template const_reference<type1>(left) == right;
}

template < class type1, class type2 >
bool operator == ( opencl::template const_reference<type1> left, opencl::template reference<type2> right )
    requires requires ( type1 a, type2 b ) { a == b; }
{
    return left == opencl::template const_reference<type2>(right);
}

template < class type1, class type2 >
bool operator == ( opencl::template const_reference<type1> left, opencl::template const_reference<type2> right )
    requires requires ( type1 a, type2 b ) { a == b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void equal_to ( __global type1* left_buf, int left_idx, __global type2* right_buf, int right_idx, __global bool* result_buf )
        {
            result_buf[0] = (left_buf[left_idx] == right_buf[right_idx]);
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "equal_to");
    auto result = boost::compute::buffer(opencl::execution_context.context(), sizeof(bool));
    kernel.set_args(left.get_buffer(), left.get_index(), right.get_buffer(), right.get_index(), result);
    opencl::execution_context.command_queue().enqueue_task(kernel);
    auto sign = boost::compute::detail::read_single_value<bool>(result, 0, opencl::execution_context.command_queue());
    opencl::execution_context.command_queue().finish();
    return sign;
}

template < class type1, class type2 >
compare_result<type1,type2> operator <=> ( opencl::template reference<type1> left, opencl::template reference<type2> right )
    requires requires ( type1 a, type2 b ) { a <=> b; }
{
    return opencl::template const_reference<type1>(left) <=> opencl::template const_reference<type2>(right);
}

template < class type1, class type2 >
compare_result<type1,type2> operator <=> ( opencl::template reference<type1> left, opencl::template const_reference<type2> right )
    requires requires ( type1 a, type2 b ) { a <=> b; }
{
    return opencl::template const_reference<type1>(left) <=> right;
}

template < class type1, class type2 >
compare_result<type1,type2> operator <=> ( opencl::template const_reference<type1> left, opencl::template reference<type2> right )
    requires requires ( type1 a, type2 b ) { a <=> b; }
{
    return left <=> opencl::template const_reference<type2>(right);
}

template < class type1, class type2 >
compare_result<type1,type2> operator <=> ( opencl::template const_reference<type1> left, opencl::template const_reference<type2> right )
    requires requires ( type1 a, type2 b ) { a <=> b; }
{
    if constexpr ( same_as<compare_result<type1,type2>,std::strong_ordering> or
                   same_as<compare_result<type1,type2>,std::weak_ordering> )
    {
        static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
            __kernel void three_way_compare ( __global type1* left_buf, int left_idx, __global type2* right_buf, int right_idx, __global int* result_buf )
            {
                result_buf[0] = left_buf[left_idx] == right_buf[right_idx] ?  0 :
                                left_buf[left_idx] <  right_buf[right_idx] ? -1 :
                                                                              1;
            }
        ), type1(), "type1", type2(), "type2");

        auto kernel = opencl::execution_context.build_kernel(program, "three_way_compare");
        auto result = boost::compute::buffer(opencl::execution_context.context(), sizeof(int));
        kernel.set_args(left.get_buffer(), left.get_index(), right.get_buffer(), right.get_index(), result);
        opencl::execution_context.command_queue().enqueue_task(kernel);
        auto sign = boost::compute::detail::read_single_value<int>(result, 0, opencl::execution_context.command_queue());
        opencl::execution_context.command_queue().finish();
        return sign ==  0 ? compare_result<type1,type2>::equivalent :
               sign == -1 ? compare_result<type1,type2>::less       :
                            compare_result<type1,type2>::greater; 
    }

    else if constexpr ( same_as<compare_result<type1,type2>,std::partial_ordering> )
    {
        static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
            __kernel void three_way_compare ( __global type1* left_buf, int left_idx, __global type2* right_buf, int right_idx, __global int* result_buf )
            {
                result_buf[0] = left_buf[left_idx] == right_buf[right_idx] ?  0 :
                                left_buf[left_idx] <  right_buf[right_idx] ? -1 :
                                left_buf[left_idx] >  right_buf[right_idx] ?  1 :
                                                                              2;
            }
        ), type1(), "type1", type2(), "type2");

        auto kernel = opencl::execution_context.build_kernel(program, "three_way_compare");
        auto result = boost::compute::buffer(opencl::execution_context.context(), sizeof(int));
        kernel.set_args(left.get_buffer(), left.get_index(), right.get_buffer(), right.get_index(), result);
        opencl::execution_context.command_queue().enqueue_task(kernel);
        auto sign = boost::compute::detail::read_single_value<int>(result, 0, opencl::execution_context.command_queue());
        opencl::execution_context.command_queue().finish();
        return sign ==  0 ? compare_result<type1,type2>::equivalent :
               sign == -1 ? compare_result<type1,type2>::less       :
               sign ==  1 ? compare_result<type1,type2>::greater    :
                            compare_result<type1,type2>::unordered; 
    }

    else
        static_assert(false, "unknown comparasion result");
}

template < class type1, class type2 >
opencl::template reference<type1> operator += ( opencl::template reference<type1> left, type2 right )
    requires requires ( type1 a, type2 b ) { a += b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void plus_assign ( __global type1* left_buf, int left_idx, type2 right_val )
        {
            left_buf[left_idx] += right_val;
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "plus_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right);
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator += ( opencl::template reference<type1> left, opencl::template reference<type2> right )
    requires requires ( type1 a, type2 b ) { a += b; }
{
    return left += opencl::template const_reference<type2>(right);
}

template < class type1, class type2 >
opencl::template reference<type1> operator += ( opencl::template reference<type1> left, opencl::template const_reference<type2> right )
    requires requires ( type1 a, type2 b ) { a += b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void plus_assign ( __global type1* left_buf, int left_idx, __global type2* right_buf, int right_idx )
        {
            left_buf[left_idx] += right_buf[right_idx];
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "plus_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right.get_buffer(), right.get_index());
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator -= ( opencl::template reference<type1> left, type2 right )
    requires requires ( type1 a, type2 b ) { a -= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void minus_assign ( __global type1* left_buf, int left_idx, type2 right_val )
        {
            left_buf[left_idx] -= right_val;
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "minus_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right);
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator -= ( opencl::template reference<type1> left, opencl::template reference<type2> right )
    requires requires ( type1 a, type2 b ) { a -= b; }
{
    return left -= opencl::template const_reference<type2>(right);
}

template < class type1, class type2 >
opencl::template reference<type1> operator -= ( opencl::template reference<type1> left, opencl::template const_reference<type2> right )
    requires requires ( type1 a, type2 b ) { a -= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void minus_assign ( __global type1* left_buf, int left_idx, __global type2* right_buf, int right_idx )
        {
            left_buf[left_idx] -= right_buf[right_idx];
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "minus_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right.get_buffer(), right.get_index());
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator *= ( opencl::template reference<type1> left, type2 right )
    requires requires ( type1 a, type2 b ) { a *= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void multiplies_assign ( __global type1* left_buf, int left_idx, type2 right_val )
        {
            left_buf[left_idx] *= right_val;
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "multiplies_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right);
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator *= ( opencl::template reference<type1> left, opencl::template reference<type2> right )
    requires requires ( type1 a, type2 b ) { a *= b; }
{
    return left *= opencl::template const_reference<type2>(right);
}

template < class type1, class type2 >
opencl::template reference<type1> operator *= ( opencl::template reference<type1> left, opencl::template const_reference<type2> right )
    requires requires ( type1 a, type2 b ) { a *= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void multiplies_assign ( __global type1* left_buf, int left_idx, __global type2* right_buf, int right_idx )
        {
            left_buf[left_idx] *= right_buf[right_idx];
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "multiplies_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right.get_buffer(), right.get_index());
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator /= ( opencl::template reference<type1> left, type2 right )
    requires requires ( type1 a, type2 b ) { a /= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void divides_assign ( __global type1* left_buf, int left_idx, type2 right_val )
        {
            left_buf[left_idx] /= right_val;
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "divides_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right);
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator /= ( opencl::template reference<type1> left, opencl::template reference<type2> right )
    requires requires ( type1 a, type2 b ) { a /= b; }
{
    return left /= opencl::template const_reference<type2>(right);
}

template < class type1, class type2 >
opencl::template reference<type1> operator /= ( opencl::template reference<type1> left, opencl::template const_reference<type2> right )
    requires requires ( type1 a, type2 b ) { a /= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void divides_assign ( __global type1* left_buf, int left_idx, __global type2* right_buf, int right_idx )
        {
            left_buf[left_idx] /= right_buf[right_idx];
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "divides_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right.get_buffer(), right.get_index());
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator %= ( opencl::template reference<type1> left, type2 right )
    requires requires ( type1 a, type2 b ) { a %= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void modulus_assign ( __global type1* left_buf, int left_idx, type2 right_val )
        {
            left_buf[left_idx] %= right_val;
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "modulus_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right);
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator %= ( opencl::template reference<type1> left, opencl::template reference<type2> right )
    requires requires ( type1 a, type2 b ) { a %= b; }
{
    return left %= opencl::template const_reference<type2>(right);
}

template < class type1, class type2 >
opencl::template reference<type1> operator %= ( opencl::template reference<type1> left, opencl::template const_reference<type2> right )
    requires requires ( type1 a, type2 b ) { a %= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void modulus_assign ( __global type1* left_buf, int left_idx, __global type2* right_buf, int right_idx )
        {
            left_buf[left_idx] %= right_buf[right_idx];
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "modulus_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right.get_buffer(), right.get_index());
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator &= ( opencl::template reference<type1> left, type2 right )
    requires requires ( type1 a, type2 b ) { a &= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void bitand_assign ( __global type1* left_buf, int left_idx, type2 right_val )
        {
            left_buf[left_idx] &= right_val;
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "bitand_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right);
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator &= ( opencl::template reference<type1> left, opencl::template reference<type2> right )
    requires requires ( type1 a, type2 b ) { a &= b; }
{
    return left &= opencl::template const_reference<type2>(right);
}

template < class type1, class type2 >
opencl::template reference<type1> operator &= ( opencl::template reference<type1> left, opencl::template const_reference<type2> right )
    requires requires ( type1 a, type2 b ) { a &= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void bitand_assign ( __global type1* left_buf, int left_idx, __global type2* right_buf, int right_idx )
        {
            left_buf[left_idx] &= right_buf[right_idx];
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "bitand_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right.get_buffer(), right.get_index());
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator |= ( opencl::template reference<type1> left, type2 right )
    requires requires ( type1 a, type2 b ) { a |= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void bitor_assign ( __global type1* left_buf, int left_idx, type2 right_val )
        {
            left_buf[left_idx] |= right_val;
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "bitor_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right);
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator |= ( opencl::template reference<type1> left, opencl::template reference<type2> right )
    requires requires ( type1 a, type2 b ) { a |= b; }
{
    return left |= opencl::template const_reference<type2>(right);
}

template < class type1, class type2 >
opencl::template reference<type1> operator |= ( opencl::template reference<type1> left, opencl::template const_reference<type2> right )
    requires requires ( type1 a, type2 b ) { a |= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void bitor_assign ( __global type1* left_buf, int left_idx, __global type2* right_buf, int right_idx )
        {
            left_buf[left_idx] |= right_buf[right_idx];
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "bitor_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right.get_buffer(), right.get_index());
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator ^= ( opencl::template reference<type1> left, type2 right )
    requires requires ( type1 a, type2 b ) { a ^= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void bitxor_assign ( __global type1* left_buf, int left_idx, type2 right_val )
        {
            left_buf[left_idx] ^= right_val;
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "bitxor_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right);
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator ^= ( opencl::template reference<type1> left, opencl::template reference<type2> right )
    requires requires ( type1 a, type2 b ) { a ^= b; }
{
    return left ^= opencl::template const_reference<type2>(right);
}

template < class type1, class type2 >
opencl::template reference<type1> operator ^= ( opencl::template reference<type1> left, opencl::template const_reference<type2> right )
    requires requires ( type1 a, type2 b ) { a ^= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void bitxor_assign ( __global type1* left_buf, int left_idx, __global type2* right_buf, int right_idx )
        {
            left_buf[left_idx] ^= right_buf[right_idx];
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "bitxor_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right.get_buffer(), right.get_index());
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator <<= ( opencl::template reference<type1> left, type2 right )
    requires requires ( type1 a, type2 b ) { a <<= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void left_shift_assign ( __global type1* left_buf, int left_idx, type2 right_val )
        {
            left_buf[left_idx] <<= right_val;
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "left_shift_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right);
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator <<= ( opencl::template reference<type1> left, opencl::template reference<type2> right )
    requires requires ( type1 a, type2 b ) { a <<= b; }
{
    return left <<= opencl::template const_reference<type2>(right);
}

template < class type1, class type2 >
opencl::template reference<type1> operator <<= ( opencl::template reference<type1> left, opencl::template const_reference<type2> right )
    requires requires ( type1 a, type2 b ) { a <<= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void left_shift_assign ( __global type1* left_buf, int left_idx, __global type2* right_buf, int right_idx )
        {
            left_buf[left_idx] <<= right_buf[right_idx];
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "left_shift_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right.get_buffer(), right.get_index());
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator >>= ( opencl::template reference<type1> left, type2 right )
    requires requires ( type1 a, type2 b ) { a >>= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void right_shift_assign ( __global type1* left_buf, int left_idx, type2 right_val )
        {
            left_buf[left_idx] >>= right_val;
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "right_shift_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right);
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type1, class type2 >
opencl::template reference<type1> operator >>= ( opencl::template reference<type1> left, opencl::template reference<type2> right )
    requires requires ( type1 a, type2 b ) { a >>= b; }
{
    return left >>= opencl::template const_reference<type2>(right);
}

template < class type1, class type2 >
opencl::template reference<type1> operator >>= ( opencl::template reference<type1> left, opencl::template const_reference<type2> right )
    requires requires ( type1 a, type2 b ) { a >>= b; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void right_shift_assign ( __global type1* left_buf, int left_idx, __global type2* right_buf, int right_idx )
        {
            left_buf[left_idx] >>= right_buf[right_idx];
        }
    ), type1(), "type1", type2(), "type2");

    auto kernel = opencl::execution_context.build_kernel(program, "right_shift_assign");
    kernel.set_args(left.get_buffer(), left.get_index(), right.get_buffer(), right.get_index());
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type >
opencl::template reference<type> operator ++ ( opencl::template reference<type> left )
    requires requires ( type a ) { ++a; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void increment ( __global type* left_buf, int left_idx )
        {
            ++left_buf[left_idx];
        }
    ), type(), "type");

    auto kernel = opencl::execution_context.build_kernel(program, "increment");
    kernel.set_args(left.get_buffer(), left.get_index());
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type > 
type operator ++ ( opencl::template reference<type> left, int )
    requires requires ( type a ) { a++; }
{
    type tmp = left;
    ++left;
    return tmp;
}

template < class type >
opencl::template reference<type> operator -- ( opencl::template reference<type> left )
    requires requires ( type a ) { --a; }
{
    static auto program = opencl::execution_context.build_program(OPENCL_SOURCE(
        __kernel void decrement ( __global type* left_buf, int left_idx )
        {
            --left_buf[left_idx];
        }
    ), type(), "type");

    auto kernel = opencl::execution_context.build_kernel(program, "decrement");
    kernel.set_args(left.get_buffer(), left.get_index());
    opencl::execution_context.command_queue().enqueue_task(kernel);
    opencl::execution_context.command_queue().finish();
    return left;
}

template < class type > 
type operator -- ( opencl::template reference<type> left, int )
    requires requires ( type a ) { a--; }
{
    type tmp = left;
    --left;
    return tmp;
}