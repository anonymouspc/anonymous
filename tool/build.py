from cppmake import *

async def build():
    if config.target == "build":
        await (await Source("main")).compile()

    if config.target == "test":
        for file in iterate_dir("./source/test"):
            await (await Executable(file)).run()