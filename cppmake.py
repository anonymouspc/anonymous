from cppmakelib import *

Package("anonymous").define_macros = {
    "abstract"   : ":",
    "extends"    : ":",
    "in"         : ":",
    "reflexpr(x)": "(^^x)",
    "self"       : "(*this)",
}

def make():
    Source(file="source/main.cpp").compile()