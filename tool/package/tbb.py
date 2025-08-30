import cppmake

async def build():
    await cppmake.include(
        name="tbb",
        dir="./package/tbb/include"
    )
    await cppmake.include(
        name="tbb",
        dir="./package/tbb/src",
        relpath="tbb/src"
    )
    await cppmake.format(
        name="tbb"
    )
