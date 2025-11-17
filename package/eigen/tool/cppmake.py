from cppmake import *

def build():
    include(
        package=Package("eigen")
        dir    ="Eigen"
    )
    include(
        package=Package("eigen")
        dir    ="unsupported/Eigen",
        relpath="unsupported/Eigen"
    )
