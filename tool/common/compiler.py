from common.config import type, compiler, compile_flags, link_flags, define_flags
from common.error  import BuildError
from common.run    import run
import os
import re
import subprocess

def preprocess_file(code_file, name=None, module_file=None):
    command = ""
    if compiler == "g++" or compiler == "clang++":
        command = f"{compiler} "                \
                  f"{' '.join(compile_flags)} " \
                  f"-E -x c++ - "               \
                  f"-o -"
        if compiler == "g++":
            if not hasattr(preprocess_file, "initialized"):
                open(f"./bin/{type}/module/mapper.txt", 'w')
                preprocess_file.initialized = True
            if name is not None and module_file is not None:
                with open(f"./bin/{type}/module/mapper.txt", 'a') as writer:
                    writer.write(f"{name} {module_file}\n")
    elif compiler == "cl":
        command = f"{compiler} "    \
                  f"/E {code_file}"

    try:
        reader = open(code_file, 'r').read()
        reader = re.sub(r'^\s*#\s*include\s+(?!<version>).*$', "", reader, flags=re.MULTILINE)
        return subprocess.run(command, shell=True, check=True, capture_output=True, text=True, input=reader).stdout
    except FileNotFoundError as e:
        raise BuildError(f"fatal error: {e.filename} not found")
    except subprocess.CalledProcessError as e:
        raise BuildError(e.stderr)
    
def compile_module(code_file, include_dirs, module_file, object_file):
    os.makedirs(os.path.dirname(module_file), exist_ok=True)
    os.makedirs(os.path.dirname(object_file), exist_ok=True)
    commands = []
    if compiler == "g++":
        commands = [f"g++ "
                    f"{' '.join(compile_flags)} "
                    f"{' '.join(f'-I {include_path}'  for include_path in include_dirs)} "
                    f"{' '.join(f'-D {key}="{value}"' for key, value   in define_flags.items())} "
                    f"-c {code_file} "
                    f"-o {object_file}"]
    elif compiler == "clang++":
        commands = [f"clang++ "
                    f"{' '.join(compile_flags)} "
                    f"{' '.join(f'-I {include_path}'  for include_path in include_dirs)} "
                    f"{' '.join(f'-D {key}="{value}"' for key, value   in define_flags.items())} "
                    f"--precompile -x c++-module {code_file} "
                    f"-o                         {module_file}",
                    
                    f"clang++ "
                    f"{' '.join(compile_flags)} "
                    f"-c {module_file} "
                    f"-o {object_file}"]
    elif compiler == "cl":
        commands = [f"cl "
                    f"{' '.join(compile_flags)} "
                    f"{' '.join(f'/I {include_path}'  for include_path in include_dirs)} "
                    f"{' '.join(f'/D {key}="{value}"' for key, value   in define_flags.items())} "
                    f"/c /interface /TP {code_file} "
                    f"/ifcOutput        {module_file} "
                    f"/Fo               {object_file}"]
    for command in commands:
        run(command)
        
def compile_source(code_file, include_dirs, object_file):
    os.makedirs(os.path.dirname(object_file), exist_ok=True)
    command = ""
    if compiler == "g++" or compiler == "clang++":
        command = f"{compiler} "                                                                 \
                  f"{' '.join(compile_flags)} "                                                  \
                  f"{' '.join(f'-I {include_path}'  for include_path in include_dirs)} "         \
                  f"{' '.join(f'-D {key}="{value}"' for key, value   in define_flags.items())} " \
                  f"-c {code_file} "                                                             \
                  f"-o {object_file}"
    elif compiler == "cl":
        command = f"cl "                                                                         \
                  f"{' '.join(compile_flags)} "                                                  \
                  f"{' '.join(f'/I {include_path}'  for include_path in include_dirs)} "         \
                  f"{' '.join(f'/D {key}="{value}"' for key, value   in define_flags.items())} " \
                  f"/c  {code_file} "                                                            \
                  f"/Fo {object_file}"
    run(command)
        
def link_object(object_files, library_files, executable_file):
    os.makedirs(os.path.dirname(executable_file), exist_ok=True)
    command = ""
    if compiler == "g++" or compiler == "clang++":
        command = f"{compiler} "                \
                  f"{' '.join(link_flags)} "    \
                  f"{' '.join(object_files)} "  \
                  f"{' '.join(library_files)} " \
                  f"-o {executable_file}"
    elif compiler == "cl":
        command = f"cl "                        \
                  f"{' '.join(link_flags)} "    \
                  f"{' '.join(object_files)} "  \
                  f"{' '.join(library_files)} " \
                  f"/Fe {executable_file}"
    run(command)
    
def run_executable(executable_file):
    run(f"./{executable_file}")