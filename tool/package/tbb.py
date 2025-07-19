from common.make import include

async def build():
    await include(
        name="tbb",
        dir="./package/tbb/include"
    )
    await include(
        name="tbb",
        dir="./package/tbb/src",
        relpath="./tbb/src"
    )
