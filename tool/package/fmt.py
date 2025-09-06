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
    await cppmake.module(
        name="fmt",
        file="./package/fmt/src/fmt.cc",
        replace={"FMT_HAS_INCLUDE": "_has_include"}
    )
