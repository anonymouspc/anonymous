from common.error import LogicError
import argparse
import os
import subprocess
import sys
import warnings

# Settings
os.chdir(f"{os.path.dirname(__file__)}/../..")
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
parser.add_argument("--type",           choices=["debug", "release"],                             default="debug"         )
parser.add_argument("--output",         choices=["executable",  "shared"],                        default="executable"    )
parser.add_argument("--compiler",                                                                 default=default_compiler)
parser.add_argument("--parallel",       type=lambda n: int(n),                                    default=os.cpu_count()  )
parser.add_argument("--verbose",        action="store_true",                                      default=False           )
parser.add_argument("--update-package", choices=["always", "new", "never"],                       default="new"           )
group = parser.add_mutually_exclusive_group()
group .add_argument("--enable-python",  action="store_true",                dest="enable_python", default=True            )
group .add_argument("--disable-python", action="store_false",               dest="enable_python", default=False           )
group = parser.add_mutually_exclusive_group()
group .add_argument("--enable-cuda",    action="store_true",                dest="enable_cuda",   default=False           )
group .add_argument("--disable-cuda",   action="store_false",               dest="enable_cuda",   default=True            )
group = parser.add_mutually_exclusive_group()
group .add_argument("--enable-opencl",  action="store_true",                dest="enable_opencl", default=False           )
group .add_argument("--disable-opencl", action="store_false",               dest="enable_opencl", default=True            )
group .add_argument("--with-opencl-lib-file")
group = parser.add_mutually_exclusive_group()
group .add_argument("--enable-vulkan",  action="store_true",                dest="enable_vulkan", default=False           )
group .add_argument("--disable-vulkan", action="store_false",               dest="enable_vulkan", default=True            )
group .add_argument("--with-vulkan")
argv = parser.parse_args()



# Compiler
compiler_info = subprocess.run(f"{argv.compiler}", shell=True, capture_output=True, text=True).stderr
if compiler_info.startswith("gcc") or compiler_info.startswith("g++"):
    compiler_name = "g++"
elif compiler_info.startswith("clang") or compiler_info.startswith("clang++"):
    compiler_name = "clang++"
elif compiler_info.startswith("Microsoft"):
    compiler_name = "cl"
else:
    raise LogicError("compiler not recognized")

# Flags
if compiler_name == "g++":
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
elif compiler_name == "clang++":
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
elif compiler_name == "cl":
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

