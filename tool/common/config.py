import argparse
import os
import sys
import warnings

# Settings

os.chdir(f"{os.path.dirname(__file__)}/../..")
os.environ["LANG"] = "en_US.UTF-8"



# Arguments
parser = argparse.ArgumentParser(description="build.py")
parser.add_argument("--type",           choices=["debug", "release"],       default="debug"       )
parser.add_argument("--output",         choices=["executable",  "shared"],  default="executable"  )
parser.add_argument("--parallel",       type=lambda n: int(n),              default=os.cpu_count())
parser.add_argument("--verbose",        action="store_true",                default=False         )
parser.add_argument("--enable-python",                                      default=True          )
parser.add_argument("--enable-cuda",                                        default=False         )
parser.add_argument("--enable-opencl",                                      default=True          )
parser.add_argument("--update-package", choices=["always", "new", "never"], default="new"         )
argv = parser.parse_args()


# System

if sys.platform == "win32":
    system            = "windows"
    compiler          = "cl"
    executable_suffix = "exe"
    shared_suffix     = "dll"
    env_seperator     = ';'
elif sys.platform == "linux":
    system            = "linux"
    compiler          = "g++"
    executable_suffix = ""
    shared_suffix     = "so"
    env_seperator     = ':'
elif sys.platform == "darwin":
    system            = "macos"
    compiler          = "clang++"
    executable_suffix = ""
    shared_suffix     = "dylib"
    env_seperator     = ':'



# Flags

if compiler == "g++":
    compile_flags = [
        "-std=c++26", 
        "-Wall",
        "-fdiagnostics-color=always",
        "-fmodules",
       f"-fmodule-mapper=./bin/{argv.type}/module/mapper.txt",
    ]
    link_flags = ["-static"]
    if argv.type == "debug":
        compile_flags += ["-g", "-O0", "-DDEBUG" ]
    elif argv.type == "release":
        compile_flags += [      "-O3", "-DNDEBUG"]
        compile_flags += ["-s"]
    if argv.output == "shared":
        link_flags += ["-shared", "-fPIC"]
    module_suffix = "gcm"
    object_suffix = "o"
    static_suffix = "a"
elif compiler == "clang++":
    compile_flags = [
        "-std=c++26", 
        "-Wall", 
        "-fdiagnostics-color=always",
       f"-fprebuilt-module-path=./bin/{argv.type}/module",
    ]
    link_flags = []
    if argv.type == "debug":
        compile_flags += ["-g", "-O0", "-DDEBUG" ]
    elif argv.type == "release":
        compile_flags += [      "-O3", "-DNDEBUG"]
        link_flags    += ["-s"]
    if argv.output == "shared":
        link_flags += ["-shared", '-fPIC']
    module_suffix = "pcm"
    object_suffix = "o"
    static_suffix = "a"
elif compiler == "cl":
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
    if argv.output == "shared":
        link_flags += ["/LD"]
    module_suffix = "ifc"
    object_suffix = "obj"
    static_suffix = "lib"

define_flags  = {
    "abstract": '0', 
    "extends" : ':',
    "in"      : ':', 
    "self"    : "(*this)"
}



# Warnings

warnings.filterwarnings("ignore", "coroutine .* was never awaited")