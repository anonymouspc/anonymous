from common.config    import argv
from common.error     import SubprocessError
from common.scheduler import scheduler
import asyncio
import sys
import time

async def run(cmd, 
              cwd            ='.',
              env            =None,
              input_stdin    =None, 
              print_stdout   =argv.verbose, 
              print_stderr   =True, 
              return_stdout  =False, 
              return_stderr  =False,
              parallel       =1,
              on_start       =None,
              on_finish      =None,
              timeout        =None):
    async with scheduler.schedule(parallel):
        if argv.dry_run and not return_stdout and not return_stderr:
            print(f">>> {' '.join(cmd)}")
            return

        if on_start is not None:
            await on_start
        if argv.verbose:
            print(f">>> {' '.join(cmd)}")

        proc = await asyncio.subprocess.create_subprocess_exec(
            *cmd,
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

        try:
            stdout = []
            stderr = []
            deadline = time.time() + timeout if timeout is not None else None
            await asyncio.wait_for(
                asyncio.gather(
                    _read_stream(stream=proc.stdout, into=stdout, tee=sys.stdout if print_stdout else None), 
                    _read_stream(stream=proc.stderr, into=stderr, tee=sys.stderr if print_stderr else None)
                ),
                timeout=deadline-time.time() if deadline is not None else None
            )
            code = await asyncio.wait_for(
                proc.wait(),
                timeout=deadline-time.time() if deadline is not None else None
            )
            stdout = "".join(stdout)
            stderr = "".join(stderr)
        except asyncio.TimeoutError:
            try:
                proc.kill()
            except ProcessLookupError:
                pass
            raise TimeoutError(f"command {' '.join(cmd)} timeout after {timeout} seconds")
            
        if on_finish is not None:
            await on_finish

        if code == 0:
            return (stdout, stderr) if return_stdout and return_stderr else \
                    stdout          if return_stdout                   else \
                            stderr  if                   return_stderr else \
                    None
        else:
            raise SubprocessError(stderr, is_stderr_printed=print_stderr)
        

    
async def _read_stream(stream, into, tee):
    while True:
        line = await stream.readline()
        if not stream.at_eof():
            line = line.decode()
            into += [line]
        else:
            break
        if tee is not None:
            print(line, end="", file=tee)