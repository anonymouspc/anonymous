module;
#include <Python.h>

export module python;

export
{
    using ::PyConfig;
    using ::PyConfig_InitPythonConfig;
    using ::PyWideStringList;
    using ::PyWideStringList_Append;
    using ::Py_IsInitialized;
    using ::Py_ssize_t;
}