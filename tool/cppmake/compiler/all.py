from cppmake.basic.config        import config
from cppmake.execution.operation import sync_wait
from cppmake.compiler.clang      import Clang
from cppmake.compiler.gcc        import Gcc
from cppmake.compiler.msvc       import Msvc
from cppmake.error.logic         import LogicError
from cppmake.system.all          import system

for Compiler in (Clang, Gcc, Msvc):
    try:
        compiler = Compiler(config.compiler)
        break
    except:
        continue
else:
    raise LogicError("unrecognized compiler")

