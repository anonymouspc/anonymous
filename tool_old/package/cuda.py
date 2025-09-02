import cppmake
import sys

async def initialize():
    if not cppmake.argv.enable_cuda:
        raise cppmake.LogicError("arg 'enable-cuda' not set but module 'cuda' imported")
    if sys.platform == "win32" or sys.platform == "linux":
        assert cppmake.compiler_id == "nvcc"
        cppmake.link_flags += ["-lOpenCL"]
    elif sys.platform == "darwin":
        assert False, "cuda is not supported on darwin"

async def build():
    await cppmake.include(
        name="cuda",
        dir="./package/cuda/libcudacxx/include"
    )
    await cppmake.include(
        name="cuda",
        dir="./package/cuda/thrust/thrust",
        relpath="thrust"
    )
    await cppmake.include(
        name="cuda",
        dir="./package/cuda/cub/cub",
        relpath="cub"
    )
    await cppmake.format(
        name="cuda",
        relpath="thrust"
    )

