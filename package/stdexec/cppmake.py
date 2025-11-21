from cppmake import *

def build():
    include(
        package=Package("stdexec"),
        dir    ="include"
    )