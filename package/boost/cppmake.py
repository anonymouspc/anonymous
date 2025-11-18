from cppmake import *

defines = {}

def build():
    cmake.build(
        package=Package("boost")
        args=[
            "-DBUILD_SHARED_LIBS=false",
           f"-DBOOST_INCLUDE_LIBRARIES=graph;polygon;spirit;stacktrace"
        ]
    )