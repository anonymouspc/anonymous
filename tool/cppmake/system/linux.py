from cppmake.compiler.gcc import Gcc
import os
import sys

class Linux:
    name              = "linux"
    executable_suffix = ""
    static_suffix     = ".a"
    shared_suffix     = ".so"
    default_compiler  = Gcc()
    env               = os.environ
    env_seperator     = ':'

    def check():
        return sys.platform == "linux"