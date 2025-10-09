import cppmake

async def build():
    await cppmake.include(
        name="fmt",
        dir="./package/fmt/include"
    )
    await cppmake.include(
        name="fmt",
        dir="./package/fmt/src"
    )