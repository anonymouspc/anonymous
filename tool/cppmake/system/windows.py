import os
import sys

class Windows:
    name              = "windows"
    executable_suffix = ".exe"
    static_suffix     = ".lib"
    shared_suffix     = ".dll"
    default_compiler  = "msvc"
    env               = os.environ
    env_seperator     = ';'

    def check():
        return sys.platform == "win32"