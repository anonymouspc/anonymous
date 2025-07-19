#undef in
#undef self
#include <pybind11/pybind11.h>
import std;
import pybind11;
import ctre;

int main ( )
{
    auto np = pybind11::module_::import("numpy");

    auto arr1 = np.attr("array")(std::vector<int>{1, 2, 3, 4, 5});
    auto arr2 = arr1 + arr1;
    std::println("print in C++: {}", arr2.cast<std::vector<int>>());
    return 42;
}

PYBIND11_MODULE(cpp, module_)
{
    module_.def("main", main);
}