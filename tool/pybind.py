from common.config   import argv, shared_suffix
from common.error    import LogicError, SubprocessError
from common.logger   import compile_output_logger
from file.shared     import Shared
from file.module     import Module
from file.object     import Object
from file.package    import Package
from file.source     import Source
import common.config
import asyncio
import shutil
import sys

async def pybind():
    common.config.argv.output = "shared"
    common.config.enable_python = True
    await Shared("main")
    await asyncio.gather(*[package.build  () for package in Package.pool.values()])
    await asyncio.gather(*[module .compile() for module  in Module .pool.values()])
    await asyncio.gather(*[source .compile() for source  in Source .pool.values()])
    await asyncio.gather(*[object .link   () for object  in Object .pool.values()])


    shutil.copyfile(f"./bin/{argv.type}/source/main.{shared_suffix}", f".cpython-{sys.version_info.major}{sys.version_info.minor}-{sys.platform}.{shared_suffix}")

if __name__ == "__main__":
    try:
        open(".log", 'w')
        asyncio.run(pybind())
    except LogicError as e:
        print(e, file=sys.stderr)
        compile_output_logger.log(str(e))
        exit(-1)
    except SubprocessError as e:
        print(e, file=sys.stderr) if not e.is_stderr_printed else None
        compile_output_logger.log(str(e))
        exit(-1)
    except KeyboardInterrupt:
        exit(-1)
    except asyncio.CancelledError:
        exit(-1)
    except:
        raise
