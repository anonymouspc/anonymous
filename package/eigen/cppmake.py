from cppmakelib import *

def package():
    include(
        package=Package("eigen"),
        dir    ="Eigen",
        relpath="Eigen"
    )
    include(
        package=Package("eigen"),
        dir    ="unsupported/Eigen",
        relpath="unsupported/Eigen"
    )
