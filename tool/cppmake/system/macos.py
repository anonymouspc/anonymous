from cppmake.compiler.clang import Clang
import os
import sys

class Macos:
    name              = "macos"
    executable_suffix = ""
    static_suffix     = ".a"
    shared_suffix     = ".dylib"
    default_compiler  = Clang()
    env               = os.environ
    env_seperator     = ':'

    def check():
        return sys.platform == "darwin"