from common.error  import LogicError, SubprocessError
from common.logger import compile_output_logger
from file.module   import Module
from file.object   import Object
from file.package  import Package
from file.source   import Source
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
        asyncio.run(build())
    except LogicError as e:
        print(e, file=sys.stderr)
        exit(-1)
    except SubprocessError as e:
        print(e, file=sys.stderr) if not e.is_stderr_printed else None
        exit(-1)
    except KeyboardInterrupt:
        exit(-1)
    except asyncio.CancelledError:
        exit(-1)
    except:
        raise
        