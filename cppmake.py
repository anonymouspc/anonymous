from cppmakelib import *

package.define_macros = {
    "abstract"   : ":",
    "extends"    : ":",
    "in"         : ":",
    "reflexpr(x)": "(^^x)",
    "self"       : "(*this)",
}

def make():
    Source("main").compile()

def test():
    for file in iterate_dir("source/test"):
        Executable(Source(file=file).name).execute()