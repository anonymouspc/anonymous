from common.error    import LogicError, SubprocessError
from file.executable import Executable
from file.module     import Module
from file.object     import Object
from file.package    import Package
from file.source     import Source
import asyncio
import os
import sys

async def test():
    try:
        await asyncio.gather(*[Executable(f"{root.removeprefix('./source/').replace('/', '.')}.{file.removesuffix(".cpp")}") for root, _, files in os.walk("./source/test") for file in files])
        await asyncio.gather(*[package   .build  () for package    in Package   .pool.values()])
        await asyncio.gather(*[module    .compile() for module     in Module    .pool.values()])
        await asyncio.gather(*[source    .compile() for source     in Source    .pool.values()])
        await asyncio.gather(*[object    .link   () for object     in Object    .pool.values()])
        await asyncio.gather(*[executable.run    () for executable in Executable.pool.values()])
    except:
        for task in asyncio.all_tasks():
            task.cancel()
        raise

if __name__ == "__main__":
    try:
        open(".log", 'w')
        asyncio.run(test())
    except LogicError as e:
        print(e, file=sys.stderr)
        print(e, file=open(".log", 'w'))
        exit(-1)
    except SubprocessError as e:
        print(e, file=sys.stderr) if not e.is_stderr_printed else None
        print(e, file=open(".log", 'a'))
        exit(-1)
    except KeyboardInterrupt as e:
        exit(-1)
    except:
        raise
