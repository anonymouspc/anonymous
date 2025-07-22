module;
#undef in
#include <xlnt/xlnt.hpp>

export module xlnt;
import        std;
import        fmt;
import        pybind11;

export namespace xlnt
{
    using xlnt::workbook;
}