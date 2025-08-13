from common.config import argv
from common.error  import LogicError
from common.make   import include
import common.config
import sys

async def initialize():
    if not argv.enable_opencl:
        raise LogicError("arg '--enable-opencl' not set but module 'opencl' imported")
    if sys.platform == "win32":
        raise LogicError("not coded yet")
    elif sys.platform == "linux":
        common.config.link_flags += ["-lOpenCL"]
    elif sys.platform == "darwin":
        common.config.link_flags += ["-framework OpenCL"]

async def build():
    await include(
        name="opencl",
        dir="./package/opencl/CL"
    )