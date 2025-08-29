from common.config import argv
from common.error  import LogicError
from common.make   import include, format
import common.config

async def initialize():
    if not argv.enable_cuda:
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
    await format(
        name="cuda",
        relpath="thrust"
    )

