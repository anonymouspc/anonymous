from cppmake.basic.context     import set_context
from cppmake.error.logic       import LogicError
from cppmake.error.process     import ProcessError
from cppmake.target.executable import Executable
from cppmake.target.module     import Module
from cppmake.target.package    import Package
from cppmake.target.source     import Source
import asyncio
import sys

def main(func):
    try:
        async def async_main():
            try:
                set_context("imag")
                await func
                set_context("real")
                await asyncio.gather(*Package   .tasks) if hasattr(Package,    "tasks") else None
                await asyncio.gather(*Module    .tasks) if hasattr(Module,     "tasks") else None
                await asyncio.gather(*Source    .tasks) if hasattr(Source,     "tasks") else None
                await asyncio.gather(*Executable.tasks) if hasattr(Executable, "tasks") else None
            except asyncio.CancelledError:
                pass
            except:
                for task in asyncio.all_tasks():
                    task.cancel()
                raise
        asyncio.run(async_main())
    except LogicError as e:
        print(e, file=sys.stderr)
        exit(-1)
    except ProcessError as e:
        print(e, file=sys.stderr) if not e.is_stderr_printed else None
        exit(-1)
    except KeyboardInterrupt:
        exit(-1)