from cppmake.error.logic   import LogicError
from cppmake.execution.run import async_run
import re

async def async_check_version(command, contains=None, matches=None):
    try:
        version = await async_run(command)
        if contains is not None and contains in version:
            return
        if matches is not None and re.match(matches, version):
            return
        raise LogicError(f"invalid compiler")
    except:
        raise LogicError(f"invalid compiler")