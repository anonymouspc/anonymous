module;
#include <concepts>

struct A { };

static auto a = A();

using B = decltype(a);

export module test;

export
{
    using ::B;
}