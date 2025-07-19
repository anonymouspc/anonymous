module;
#undef in
#undef self
#include <pybind11/embed.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

export module pybind11;
import        std;
import        eigen;
import        python;

export namespace pybind11
{
    using pybind11::error_already_set;
    using pybind11::make_tuple;
    using pybind11::module_;
    using pybind11::scoped_interpreter;

    inline auto interpreter = [] -> std::optional<pybind11::scoped_interpreter>
    {
        if ( not Py_IsInitialized() )
        {
            auto conf = PyConfig();
            PyConfig_InitPythonConfig(&conf);

            conf.install_signal_handlers = 1;
            conf.parse_argv              = 0;
            conf.pythonpath_env          = new wchar_t[sizeof(PYTHONPATH)/sizeof(wchar_t)] {PYTHONPATH};
            conf.site_import             = 1;

            return pybind11::scoped_interpreter(&conf);
        }
        else
        {
            return std::nullopt;
        }
    } ();
}
