module;
#undef in
#undef self
#ifndef _GNU_SOURCE
    #define BOOST_STACKTRACE_GNU_SOURCE_NOT_REQUIRED
#endif
#include <boost/stacktrace.hpp>

export module boost.stacktrace;
// import std; This module might be depended by std:feature.stacktrace by std:feature by std.

export namespace boost::stacktrace
{
    using boost::stacktrace::frame;
    using boost::stacktrace::stacktrace;
}