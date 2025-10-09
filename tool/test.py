import cppmake
import asyncio

async def test():
    for name in cppmake.iterate_dir("./source/test", recursive=True, file_only=True):
        name = name.removeprefix("./source")
        name = name.removesuffix(".cpp")
        await (await cppmake.Executable(name)).run()

cppmake.main(test())