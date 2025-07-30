from common.config import argv, compiler_name
from common.error  import LogicError
from common.make   import include, lib
import common.config
import sys

async def initialize():
    if not argv.enable_opencl:
        raise LogicError("arg `--disable-opencl` set but package `opencl` imported")
    
    if sys.platform == "win32":
        raise LogicError("not coded yet")
    elif sys.platform == "linux":
        common.config.link_flags += ["-lOpenCL"]
    elif sys.platform == "darwin":
        common.config.link_flags += ["-framework OpenCL"]
    common.config.define_flags["ENABLE_OPENCL"] = "true"

async def build():
    await include(
        name="opencl",
        dir="./package/opencl/CL"
    )