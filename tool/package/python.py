from common.config import argv, shared_suffix, env_seperator
from common.error  import LogicError
from common.make   import include, lib
import common.config
import site
import sys
import sysconfig

async def initialize():
    if not argv.enable_python:
        raise LogicError("arg '--enable-python' not set but module 'python' imported")
    common.config.defines["PYTHONPATH"] = f'L"{env_seperator.join([pythonpath for pythonpath in site.getsitepackages()])}"'


async def build():
    await include(
        name="python",
        dir=f"{sysconfig.get_config_var("INCLUDEPY")}"
    )
    await lib(
        name="python",
        file=f"{sysconfig.get_config_var("LIBDIR")}/libpython{sys.version_info.major}.{sys.version_info.minor}.{shared_suffix}"
    )

