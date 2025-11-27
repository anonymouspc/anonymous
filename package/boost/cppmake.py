from cppmakelib import *

if type(compiler) is Gcc:
    package.compile_flags += ["-Wno-deprecated-variadic-comma-omission"]
if type(compiler) is Clang:
    package.compile_flags += ["-Wno-deprecated-missing-comma-variadic-parameter"]

def build():
    cmake.build(
        package=package,
        args=[
            "-DBUILD_SHARED_LIBS=false",
        ]
    )