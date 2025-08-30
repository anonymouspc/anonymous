import cppmake
import site
import sys
import sysconfig

async def initialize():
    if not cppmake.argv.enable_python:
        raise cppmake.LogicError("arg '--enable-python' not set but module 'python' imported")
    cppmake.defines["PYTHONPATH"] = f'L"{cppmake.env_seperator.join([pythonpath for pythonpath in site.getsitepackages()])}"'

async def build():
    await cppmake.include(
        name="python",
        dir=f"{sysconfig.get_config_var("INCLUDEPY")}"
    )
    await cppmake.lib(
        name="python",
        file=f"{sysconfig.get_config_var("LIBDIR")}/libpython{sys.version_info.major}.{sys.version_info.minor}.{cppmake.shared_suffix}"
    )
    await format(
        name="python"
    )

