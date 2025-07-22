from common.error  import SubprocessError
from common.config import argv
from common.scheduler import scheduler
import asyncio
import os
import sys

async def run(cmd, 
              cwd            ='.',
              env            =os.environ.copy(),
              input_stdin    =None, 
              print_stdout   =argv.verbose, 
              print_stderr   =True, 
              return_stdout  =False, 
              return_stderr  =False,
              parallel       =1,
              on_start       =None,
              on_finish      =None):
    async with scheduler.schedule(parallel):
        if on_start is not None:
            await on_start

        if argv.verbose:
            print(cmd)
        proc = await asyncio.subprocess.create_subprocess_shell(
            cmd=cmd,
            cwd=cwd,
            env=env,
            stdin =asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        if input_stdin is not None:
            proc.stdin.write(input_stdin.encode())
            await proc.stdin.drain()
        proc.stdin.close()

        async def read(stream, into, tee):
            while True:
                line = await stream.readline()
                if not stream.at_eof():
                    line = line.decode()
                    into += [line]
                else:
                    break
                if tee is not None:
                    print(line, end="", file=tee)
        stdout = []
        stderr = []
        await asyncio.gather(
            read(stream=proc.stdout, into=stdout, tee=sys.stdout if print_stdout else None), 
            read(stream=proc.stderr, into=stderr, tee=sys.stderr if print_stderr else None)
        )
        stdout = "".join(stdout)
        stderr = "".join(stderr)

        code = await proc.wait()
        if on_finish is not None:
            await on_finish

        if code == 0:
            return (stdout, stderr) if return_stdout and return_stderr else \
                    stdout          if return_stdout                   else \
                            stderr  if                   return_stderr else \
                    None
        else:
            raise SubprocessError(stderr, is_stderr_printed=print_stderr)
