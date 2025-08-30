import cppmake
import sys

async def initialize():
    if not cppmake.argv.enable_opencl:
        raise cppmake.LogicError("arg '--enable-opencl' not set but module 'opencl' imported")
    if sys.platform == "win32":
        cppmake.link_flags += ["/L OpenCL"]
    elif sys.platform == "linux":
        cppmake.link_flags += ["-lOpenCL"]
    elif sys.platform == "darwin":
        cppmake.link_flags += ["-framework OpenCL"]

async def build():
    await cppmake.include(
        name="opencl",
        dir="./package/opencl/CL",
        relpath="CL"
    )