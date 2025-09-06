from cppmake.basic.config import config

define = {
    "abstract"   : '0', 
    "extends"    : ':',
    "in"         : ':',
    "reflexpr(x)": "(^^x)",
    "self"       : "(*this)"
}
if config.enable_python:
    define["ENABLE_PYTHON"] = "true"
if config.enable_opencl:
    define["ENABLE_OPENCL"] = "true"
if config.enable_cuda:
    define["ENABLE_CUDA"  ] = "true"
