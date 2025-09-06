from cppmake.basic.config   import config
from cppmake.compiler.clang import Clang
from cppmake.compiler.gcc   import Gcc
from cppmake.compiler.msvc  import Msvc
from cppmake.error.logic    import LogicError
from cppmake.system.all     import system

if config.compiler == "":
    compiler = system.default_compiler
else:
    if Clang.check(config.compiler):
        compiler = Clang(config.compiler)
    elif Gcc.check(config.compiler):
        compiler = Gcc(config.compiler)
    elif Msvc.check(config.compiler):
        compiler = Msvc(config.compiler)
    else:
        raise LogicError("unrecognized compiler")
