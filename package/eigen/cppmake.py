from cppmakelib import *

def build():
    include(
        package=package,
        dir    ="Eigen",
        relpath="Eigen"
    )
    include(
        package=package,
        dir    ="unsupported/Eigen",
        relpath="unsupported/Eigen"
    )
