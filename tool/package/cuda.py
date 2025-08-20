from common.config import argv
from common.error  import LogicError
from common.make   import include

async def initialize():
    if not argv.enable_python:
        raise LogicError("arg 'enable-cuda' not set but module 'cuda' imported")

async def build():
    await include(
        name="cuda",
        dir="./package/cuda/libcudacxx/include"
    )
    await include(
        name="cuda",
        dir="./package/cuda/thrust/thrust",
        relpath="thrust"
    )
    await include(
        name="cuda",
        dir="./package/cuda/cub/cub",
        relpath="cub"
    )

