from cppmake.basic.config            import config
from cppmake.error.subprocess        import SubprocessError
from cppmake.logger.compile_commands import compile_commands_logger
from cppmake.logger.compile_outputs  import compile_outputs_logger
from cppmake.utility.decorator       import syncable
import asyncio
import sys
import time

def             run(*args, **kwargs): ...
async def async_run(*args, **kwargs): ...



@syncable
async def async_run(
    command,
    cwd           ='.', 
    env           =None,
    print_command =config.verbose,
    log_command   =False, # or (True, code_file)
    run_command   =True,
    print_stdout  =config.verbose,
    log_stdout    =False, # or True, or (True, processor)
    return_stdout =False,
    print_stderr  =True,
    log_stderr    =False, # or True, or (True, processor)
    return_stderr =False,
    check         =True,
    timeout       =None
):
    if print_command:
        print(f">>> {' '.join(command)}")
    if type(log_command) == bool and log_command == True:
        assert False
    if type(log_command) == tuple and log_command[0] == True:
        compile_commands_logger.log_command(command=command, code_file=log_command[1])
    if run_command:
        proc = await asyncio.subprocess.create_subprocess_exec(
           *command,
            cwd=cwd,
            env=env,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
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
            raise TimeoutError(f"process {' '.join(command)} timeouts after {timeout} seconds")
        if (type(log_stdout) == bool  and log_stdout    == True) or \
           (type(log_stdout) == tuple and log_stdout[0] == True):
            compile_outputs_logger.log_output(stdout if type(log_stdout) == bool else log_stdout[1](stdout))
        if (type(log_stderr) == bool  and log_stderr    == True) or \
           (type(log_stderr) == tuple and log_stderr[0] == True):
            compile_outputs_logger.log_output(stderr if type(log_stderr) == bool else log_stderr[1](stderr))
        if not check or code == 0:
            return (stdout, stderr) if return_stdout and return_stderr else \
                    stdout          if return_stdout                   else \
                            stderr  if                   return_stderr else \
                    None
        else:
            compile_outputs_logger.log_output(output=stderr)
            raise SubprocessError(code=code, stderr=stderr, is_stderr_printed=print_stderr)