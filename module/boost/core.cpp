module;
#undef in
#include <boost/core/addressof.hpp>
#include <boost/core/alignof.hpp>
#include <boost/core/alloc_construct.hpp>
#include <boost/core/allocator_access.hpp>
#include <boost/core/allocator_traits.hpp>
#include <boost/core/bit.hpp>
#include <boost/core/checked_delete.hpp>
#include <boost/core/cmath.hpp>
#include <boost/core/data.hpp>
#include <boost/core/default_allocator.hpp>
#include <boost/core/demangle.hpp>
#include <boost/core/empty_value.hpp>
#include <boost/core/enable_if.hpp>
#include <boost/core/exchange.hpp>
#include <boost/core/explicit_operator_bool.hpp>
#include <boost/core/fclose_deleter.hpp>
#include <boost/core/first_scalar.hpp>
#include <boost/core/functor.hpp>
#include <boost/core/identity.hpp>
#include <boost/core/ignore_unused.hpp>
#include <boost/core/invoke_swap.hpp>
// #include <boost/core/is_same.hpp>
#include <boost/core/launder.hpp>
#include <boost/core/lightweight_test_trait.hpp>
#include <boost/core/lightweight_test.hpp>
#include <boost/core/make_span.hpp>
#include <boost/core/max_align.hpp>
#include <boost/core/memory_resource.hpp>
#include <boost/core/no_exceptions_support.hpp>
#include <boost/core/noinit_adaptor.hpp>
#include <boost/core/noncopyable.hpp>
#include <boost/core/null_deleter.hpp>
#include <boost/core/nvp.hpp>
#include <boost/core/pointer_in_range.hpp>
#include <boost/core/pointer_traits.hpp>
#include <boost/core/quick_exit.hpp>
#include <boost/core/ref.hpp>
#include <boost/core/scoped_enum.hpp>
#include <boost/core/serialization.hpp>
#include <boost/core/size.hpp>
#include <boost/core/snprintf.hpp>
#include <boost/core/span.hpp>
// #include <boost/core/swap.hpp>
#include <boost/core/type_name.hpp>
#include <boost/core/typeinfo.hpp>
#include <boost/core/uncaught_exceptions.hpp>
#include <boost/core/underlying_type.hpp>
#include <boost/core/use_default.hpp>
#include <boost/core/verbose_terminate_handler.hpp>
#include <boost/core/yield_primitives.hpp>

export module boost.core;
// import std; This module might be depended by std:extension.formatter by std:extension by std.
export namespace boost::core
{
    using boost::core::demangle;
}