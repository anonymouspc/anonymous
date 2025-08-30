import argparse
import os
import subprocess
import sys
import warnings

# Settings
os.chdir(f"{os.path.dirname(__file__)}/../../..")
os.environ["LANG"] = "en_US.UTF-8"



# System
if sys.platform == "win32":
    default_compiler  = "cl"
    executable_suffix = "exe"
    shared_suffix     = "dll"
    env_seperator     = ';'
elif sys.platform == "linux":
    default_compiler  = "g++"
    executable_suffix = ""
    shared_suffix     = "so"
    env_seperator     = ':'
elif sys.platform == "darwin":
    default_compiler  = "clang++"
    executable_suffix = ""
    shared_suffix     = "dylib"
    env_seperator     = ':'



# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--type",           choices=["debug", "release", "size"],                     default="debug"         )
parser.add_argument("--compiler",                                                                 default=default_compiler)
parser.add_argument("--parallel",       type=lambda n: int(n),                                    default=os.cpu_count()  )
parser.add_argument("--update-package", action="store_true",                                      default=False           )
group = parser.add_mutually_exclusive_group()
group .add_argument("--verbose",        action="store_true",                                      default=False           )
group .add_argument("--dry-run",        action="store_true",                                      default=False           )
group = parser.add_mutually_exclusive_group()
group .add_argument("--enable-python",  action="store_true",                dest="enable_python", default=False           )
group .add_argument("--disable-python", action="store_false",               dest="enable_python", default=True            )
group = parser.add_mutually_exclusive_group()
group .add_argument("--enable-opencl",  action="store_true",                dest="enable_opencl", default=False           )
group .add_argument("--disable-opencl", action="store_false",               dest="enable_opencl", default=True            )
group = parser.add_mutually_exclusive_group()
group .add_argument("--enable-cuda",    action="store_true",                dest="enable_cuda",   default=False           )
group .add_argument("--disable-cuda",   action="store_false",               dest="enable_cuda",   default=True            )
argv = parser.parse_args()


# Compiler
compiler_info = subprocess.run(f"{argv.compiler}", shell=True, capture_output=True, text=True).stderr
if compiler_info.startswith("gcc") or compiler_info.startswith("g++"):
    compiler_id = "g++"
elif compiler_info.startswith("clang") or compiler_info.startswith("clang++"):
    compiler_id = "clang++"
elif compiler_info.startswith("Microsoft"):
    compiler_id = "cl"
else:
    assert False, f"compiler {argv.compiler} not recognized"



# Flags
if compiler_id == "g++":
    compile_flags = [
        "-std=c++26", 
        "-Wall",
        "-fdiagnostics-color=always",
        "-fmodules",
        "-fmodule-mapper=./bin/cache/module_mapper.txt",
        "-Wno-global-module",
        "-Wno-deprecated-variadic-comma-omission"
    ]
    link_flags = ["-lstdc++exp"]
    if argv.type == "debug":
        compile_flags += ["-g", "-O0", "-DDEBUG", "-fno-inline"]
    elif argv.type == "release":
        compile_flags += [      "-O3", "-DNDEBUG"]
        link_flags    += ["-s"]
    elif argv.type == "size":
        compile_flags += [      "-Os"]
    module_suffix = "gcm"
    object_suffix = "o"
    static_suffix = "a"
elif compiler_id == "clang++":
    compile_flags = [
        "-std=c++26", 
        "-Wall", 
        "-fdiagnostics-color=always",
       f"-fprebuilt-module-path=./bin/{argv.type}/module",
        "-Wno-reserved-module-identifier",
        "-Wno-deprecated-missing-comma-variadic-parameter"
    ]
    link_flags = []
    if argv.type == "debug":
        compile_flags += ["-g", "-O0", "-DDEBUG", "-fno-inline"]
    elif argv.type == "release":
        compile_flags += [      "-O3", "-DNDEBUG"]
        link_flags    += ["-s"]
    elif argv.type == "size":
        compile_flags += [      "-Os"]
    module_suffix = "pcm"
    object_suffix = "o"
    static_suffix = "a"
elif compiler_id == "cl":
    compile_flags = [
        "/std:c++latest",
        "/EHsc",
        "/W4"
    ]
    link_flags = ["/MT"]
    if argv.type == "debug":
        compile_flags += ["/Z7", "/Od", "/DDEBUG" ]
    elif argv.type == "release":
        compile_flags += [       "/O2", "/DNDEBUG"]
    elif argv.type == "size":
        compile_flags += [       "/O1"]
    module_suffix = "ifc"
    object_suffix = "obj"
    static_suffix = "lib"



# Specialize
if sys.platform == "linux":
    assert compiler_id == "g++" or compiler_id == "clang++"
    link_flags += ["-fuse-ld=lld"]
elif sys.platform == "darwin":
    assert compiler_id == "g++" or compiler_id == "clang++"
    link_flags += ["-w"]




# Define
defines = {
    "abstract"   : '0', 
    "extends"    : ':',
    "in"         : ':',
    "reflexpr(x)": "(^^x)",
    "self"       : "(*this)"
}
if argv.enable_python:
    defines["ENABLE_PYTHON"] = "true"
if argv.enable_opencl:
    defines["ENABLE_OPENCL"] = "true"
if argv.enable_cuda:
    defines["ENABLE_CUDA"  ] = "true"


# Warnings
warnings.filterwarnings("ignore", "coroutine .* was never awaited")
