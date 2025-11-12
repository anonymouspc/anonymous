from cppmake.basic.config            import config
from cppmake.error.process           import ProcessError
from cppmake.logger.compile_commands import compile_commands_logger
from cppmake.logger.compile_outputs  import compile_outputs_logger
import asyncio
import sys
import time

# Every project has its own kind of shit mountain,
# and the main difference between them is where these mountains are placed. 
# Some put it in an obvious place that is transparent to users
# (for example, C++ template, which "zero-cost" exposes every bit
# of mess from their inner implementations), 
# while others hide them in a corner where no one can reach
# (for example, the Python GIL).
#
# Here, in this project, we've gathered and hid
# all our shit in the file below. :)

async def async_run(
    command,
    cwd           ='.', 
    env           =None,
    print_command =config.verbose or config.dry_run,
    log_command   =False, # or (True, code_file)
    run_command   =not config.dry_run,
    print_stdout  =config.verbose,
    log_stdout    =False, # or True, or (True, processor)
    return_stdout =False,
    print_stderr  =True,
    log_stderr    =False, # or True, or (True, processor)
    return_stderr =False,
    timeout       =None
):
    if print_command:
        print(f">>> {' '.join(command)}")
    assert not (type(log_command) is bool and log_command == True)
    if type(log_command) is tuple and log_command[0] == True:
        compile_commands_logger.log(command=command, code_file=log_command[1])
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
        if (type(log_stdout) is bool  and log_stdout    == True) or \
           (type(log_stdout) is tuple and log_stdout[0] == True):
            compile_outputs_logger.log(stdout if type(log_stdout) is bool else log_stdout[1](stdout))
        if (type(log_stderr) is bool  and log_stderr    == True) or \
           (type(log_stderr) is tuple and log_stderr[0] == True):
            compile_outputs_logger.log(stderr if type(log_stderr) is bool else log_stderr[1](stderr))
        if code == 0:
            return (stdout, stderr) if return_stdout and return_stderr else \
                    stdout          if return_stdout                   else \
                            stderr  if                   return_stderr else \
                    None
        else:
            compile_outputs_logger.log(stderr)
            raise ProcessError(stderr, is_stderr_printed=print_stderr)