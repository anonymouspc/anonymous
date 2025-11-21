from cppmakelib import *

if type(compiler) is Gcc:
    Package("boost").compile_flags += ["-Wno-deprecated-variadic-comma-omission"]
if type(compiler) is Clang:
    Package("boost").compile_flags += ["-Wno-deprecated-missing-comma-variadic-parameter"]

def package():
    cmake.build(
        package=Package("boost"),
        args=[
            "-DBUILD_SHARED_LIBS=false",
        ]
    )