from common.config import system
from common.make   import include
import common.config

async def initialize():
    if system == "windows" or system == "linux":
        common.config.link_flags += ["-lOpenCL"]
    if system == "macos":
        common.config.link_flags += ["-framework OpenCL"]

async def build():
    await include(
        name="opencl",
        dir="./package/opencl/CL"
    )