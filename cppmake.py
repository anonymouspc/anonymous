from cppmake import *

define_macros = {
    "in": ':'
}

import_packages = [
    "bzip2"
]

Source("main").compile()