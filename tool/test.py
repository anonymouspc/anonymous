import cppmake

async def test():
    await cppmake.when_all(*[
        (await cppmake.Executable(name)).run()
        async for file in cppmake.iterate_dir("./source/test")
        for name in [file.removeprefix("./source/test").removesuffix(".cpp")]
    ])

cppmake.sync_wait(test())