from common.error import LogicError, SubprocessError
from file.module  import Module
from file.object  import Object
from file.package import Package
from file.source  import Source
import asyncio
import sys

async def build():
    try:
        await Object("main")
        await asyncio.gather(*[package.build  () for package in Package.pool.values()])
        await asyncio.gather(*[module .compile() for module  in Module .pool.values()])
        await asyncio.gather(*[source .compile() for source  in Source .pool.values()])
        await asyncio.gather(*[object .link   () for object  in Object .pool.values()])
    except:
        for task in asyncio.all_tasks():
            task.cancel()
        raise

if __name__ == "__main__":
    try:
        open(".log", 'w')
        asyncio.run(build())
    except LogicError as e:
        print(e, file=sys.stderr)
        print(e, file=open(".log", 'a'))
        exit(-1)
    except SubprocessError as e:
        print(e, file=sys.stderr) if not e.is_stderr_printed else None
        print(e, file=open(".log", 'a'))
        exit(-1)
    except KeyboardInterrupt as e:
        exit(-1)
    except:
        raise
        