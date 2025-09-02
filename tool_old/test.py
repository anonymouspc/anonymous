import cppmake
import asyncio

async def test():
    async for file in cppmake.iterate_dir("./source/test", recursive=True, file_only=True):
        name = file.removeprefix("./source/test") \
                   .removesuffix(".cpp")
        await cppmake.Executable(name).run()
    await asyncio.gather(*[
        cppmake.Executable(name)
        for name in file
        async for file in cppmake.iterate
    ])

cppmake.wait(test())