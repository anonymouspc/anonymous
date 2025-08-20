module;
#undef in
#undef self
#undef extends
#if defined(__GNUC__) and not defined(__clang__)
    #pragma GCC diagnostic ignored "-Wdeprecated-variadic-comma-omission"
#elifdef __clang__
    #pragma clang diagnostic ignored "-Wdeprecated-missing-comma-variadic-parameter"
#endif
#define BOOST_COMPUTE_USE_CPP11
#include <boost/compute.hpp>

export module boost.compute;
import        std;
import opencl;

export namespace boost::compute
{
    using boost::compute::system;
}