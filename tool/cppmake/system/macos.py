import os
import sys

class Macos:
    name              = "macos"
    executable_suffix = ""
    static_suffix     = ".a"
    shared_suffix     = ".dylib"
    default_compiler  = "clang"
    env               = os.environ
    env_seperator     = ':'

    def check():
        return sys.platform == "darwin"