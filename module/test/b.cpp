module;
#include "a.cpp"

export module test.b;

export namespace test
{
    using test::a;
}