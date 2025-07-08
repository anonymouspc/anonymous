module;
#undef in
#undef self
#if defined(__GNUC__) and not defined(__clang__)
    #pragma GCC diagnostic ignored "-Wdeprecated-declarations"
    #pragma GCC diagnostic ignored "-Wdeprecated-variadic-comma-omission"
#elifdef __clang__
    #pragma clang diagnostic ignored "-Wdeprecated-missing-comma-variadic-parameter"
    #pragma clang diagnostic ignored "-Wunused-private-field"
#endif
#include <boost/beast.hpp>

export module boost.beast;
import boost.asio;
import boost.system;
import std;

export namespace boost::beast
{
    
}