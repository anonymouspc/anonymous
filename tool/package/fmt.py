from common.make import include, module

async def build():
    await include(
        name="fmt",
        dir="./package/fmt/include"
    )
    await include(
        name="fmt",
        dir="./package/fmt/src"
    )
    await module(
        name="fmt",
        file="./package/fmt/src/fmt.cc",
        replace={"FMT_HAS_INCLUDE": "__has_include"}
    )
