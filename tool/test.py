import cppmake
import asyncio

async def test():
    await asyncio.gather(*[
        (await cppmake.Executable(name)).run()
        for file in cppmake.iterate_dir("./source/test", file_only=True, recursive=True)
        for name in [file.removeprefix("./source/").removesuffix(".cpp")]
    ])

cppmake.main(test())