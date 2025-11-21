from cppmakelib import *

if type(compiler) is Clang:
    Package("std").compile_flags += ["-Wno-reserved-module-identifier"]
        
        