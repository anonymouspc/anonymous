#undef in
#undef self
#include <pybind11/pybind11.h>
import std;
import pybind11;
import ctre;

int main ( )
{
    std::cout << ctre::match<"[a-z]+">("hello") << std::endl;
}

PYBIND11_MODULE(cpp, module_)
{
    module_.def("main", main);
}