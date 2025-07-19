from common.make import include

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

