import os
import sys

class Linux:
    name              = "linux"
    executable_suffix = ""
    static_suffix     = ".a"
    shared_suffix     = ".so"
    compiler_name     = "gcc"
    env               = os.environ
    env_seperator     = ':'

    def check():
        return sys.platform == "linux"