from common.error    import BuildError
from file.executable import Executable
from file.module     import Module
from file.object     import Object
from file.package    import Package
from file.source     import Source
import asyncio
import os
import sys

if __name__ == "__main__":
    async def test():
        open(".log", 'w')
        await asyncio.gather(*[Executable(f"{root.removeprefix('./source/').replace('/', '.')}.{file.removesuffix(".cpp")}") for root, _, files in os.walk("./source/test") for file in files])
        await asyncio.gather(*[package   .build  () for package    in Package   .pool.values()])
        await asyncio.gather(*[module    .compile() for module     in Module    .pool.values()])
        await asyncio.gather(*[source    .compile() for source     in Source    .pool.values()])
        await asyncio.gather(*[object    .link   () for object     in Object    .pool.values()])
        await asyncio.gather(*[executable.run    () for executable in Executable.pool.values()])
                
    try:
        asyncio.run(test())
    except BuildError as e:
        print(e, end="", file=open(".log", 'a'))
        exit(-1)
    except KeyboardInterrupt as e:
        exit(-1)
    except:
        raise
