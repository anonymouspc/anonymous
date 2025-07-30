from common.config import argv, env_seperator, shared_suffix
from common.error  import LogicError
from common.make   import include, lib
import common.config
import site
import sys
import sysconfig

async def initialize():
    if not argv.enable_python:
        raise LogicError("arg `--disable-python` set but package `python` imported")
    
    common.config.define_flags["ENABLE_PYTHON"] = "true"
    common.config.define_flags["PYTHONPATH"] = f'L\\"{env_seperator.join([pythonpath for pythonpath in site.getsitepackages()])}\\"'

async def build():
    await include(
        name="python",
        dir=f"{sysconfig.get_config_var("INCLUDEPY")}"
    )
    await lib(
        name="python",
        file=f"{sysconfig.get_config_var("LIBDIR")}/libpython{sys.version_info.major}.{sys.version_info.minor}.{shared_suffix}"
    )

