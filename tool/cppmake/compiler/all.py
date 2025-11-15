from cppmake.basic.config   import config
from cppmake.compiler.clang import Clang
from cppmake.compiler.gcc   import Gcc
from cppmake.compiler.msvc  import Msvc
from cppmake.error.config   import ConfigError

compiler = ...



suberrors = []
for Compiler in (Clang, Gcc, Msvc):
    try:
        compiler = Compiler(config.compiler)
        break
    except ConfigError as e:
        suberrors += [e]
else:
    raise ConfigError(
        f'compiler "{config.compiler}" is not supported, because\n'
        ''.join([f'  {error}\n' for error in suberrors])
    )

