from common.config import argv
from common.error  import LogicError
from common.make   import include
import common.config

async def initialize():
    if not argv.enable_python:
        raise LogicError("arg `--disable-cuda` set but package `cuda` imported")
    common.config.define_flags["ENABLE_CUDA"] = "true"

async def build():
    await include(
        name="cuda",
        dir="./package/cuda/libcudacxx/include"
    )
    await include(
        name="cuda",
        dir="./package/cuda/thrust/thrust",
        relpath="./thrust"
    )
    await include(
        name="cuda",
        dir="./package/cuda/cub/cub",
        relpath="./cub"
    )

