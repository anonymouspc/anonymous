from cppmake.basic.config            import config
from cppmake.error.process           import ProcessError
from cppmake.logger.compile_commands import compile_commands_logger
from cppmake.logger.compile_outputs  import compile_outputs_logger
import asyncio
import sys
import time

async def run_process(
    command, 
    cwd           ='.', 
    env           =None,
    print_command =config.verbose or config.dry_run,
    log_command   =(False, None),
    run_command   =not config.dry_run,
    input_stdin   =None,
    print_stdout  =config.verbose,
    print_stderr  =True,
    return_stdout =False,
    return_stderr =False,
    timeout       =None
):
    if print_command:
        print(f">>> {' '.join(command)}")
    if log_command[0] is True:
        compile_commands_logger.log(command=command, code_file=log_command[1])
    if run_command:
        proc = await asyncio.subprocess.create_subprocess_exec(
            *command,
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
            async def read_stream(stream, into, tee):
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
            deadline = time.time() + timeout if timeout is not None else None
            await asyncio.wait_for(
                asyncio.gather(
                    read_stream(stream=proc.stdout, into=stdout, tee=sys.stdout if print_stdout else None), 
                    read_stream(stream=proc.stderr, into=stderr, tee=sys.stderr if print_stderr else None)
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
            raise TimeoutError(f"command {' '.join(command)} timeout after {timeout} seconds")
        if code == 0:
            return (stdout, stderr) if return_stdout and return_stderr else \
                    stdout          if return_stdout                   else \
                            stderr  if                   return_stderr else \
                    None
        else:
            compile_outputs_logger.log(stderr)
            raise ProcessError(stderr, is_stderr_printed=print_stderr)
        
def run_process_sync(*args, **kwargs):
    return asyncio.run(run_process(*args, **kwargs))