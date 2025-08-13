from common.config import argv, compiler_id, compile_flags, link_flags, defines
from common.error  import LogicError
from common.logger import compile_commands_logger, module_mapper_logger
from common.run    import run
import os
import re

async def preprocess_file(code_file, name=None, module_file=None, **run_args):
    command = ""
    if compiler_id == "g++" or compiler_id == "clang++":
        command = f"{argv.compiler} "                                                     \
                  f"{' '.join(compile_flags)} "                                           \
                  f"{' '.join(f'-D {key}="{value}"' for key, value in defines.items())} " \
                  f"-E -x c++ - "                                                         \
                  f"-o -"
    elif compiler_id == "cl":
        command = f"{argv.compiler} "                                                     \
                  f"{' '.join(f'/D {key}="{value}"' for key, value in defines.items())} " \
                  f"/E -"
    try:
        content = open(code_file, 'r').read()
        content = re.sub(r'^\s*#\s*include\s+(?!<version>).*$', "", content, flags=re.MULTILINE)
    except FileNotFoundError as e:
        raise LogicError(f"file {e.filename} not found")
    if name is not None and module_file is not None:
        module_mapper_logger.log(name=name, file=module_file)
    return await run(command, input_stdin=content, print_stdout=False, return_stdout=True, **run_args)
    
async def compile_module(code_file, include_dirs, module_file, object_file, **run_args):
    os.makedirs(os.path.dirname(module_file), exist_ok=True)
    os.makedirs(os.path.dirname(object_file), exist_ok=True)
    command = ""
    if compiler_id == "g++":
        command = f"{argv.compiler} "                                                       \
                  f"{' '.join(compile_flags)} "                                             \
                  f"{' '.join(f'-I {include_path}'  for include_path in include_dirs)} "    \
                  f"{' '.join(f'-D {key}="{value}"' for key, value   in defines.items())} " \
                  f"-c {code_file} "                                                        \
                  f"-o {object_file}"
    elif compiler_id == "clang++":
        command = f"{argv.compiler} "                                                       \
                  f"{' '.join(compile_flags)} "                                             \
                  f"{' '.join(f'-I {include_path}'  for include_path in include_dirs)} "    \
                  f"{' '.join(f'-D {key}="{value}"' for key, value   in defines.items())} " \
                  f"--precompile -x c++-module {code_file} "                                \
                  f"-o                         {module_file} "                              \
                   "&& "                                                                    \
                  f"{argv.compiler} "                                                       \
                  f"{' '.join(compile_flags)} "                                             \
                  f"-c {module_file} "                                                      \
                  f"-o {object_file}"
    elif compiler_id == "cl":
        command = f"{argv.compiler} "                                                       \
                  f"{' '.join(compile_flags)} "                                             \
                  f"{' '.join(f'/I {include_path}'  for include_path in include_dirs)} "    \
                  f"{' '.join(f'/D {key}="{value}"' for key, value   in defines.items())} " \
                  f"/c /interface /TP {code_file} "                                         \
                  f"/ifcOutput        {module_file} "                                       \
                  f"/Fo               {object_file}"
    compile_commands_logger.log(file=code_file, command=command.partition("&&")[0])
    await run(command, **run_args)

async def compile_source(code_file, include_dirs, object_file, **run_args):
    os.makedirs(os.path.dirname(object_file), exist_ok=True)
    command = ""
    if compiler_id == "g++" or compiler_id == "clang++":
        command = f"{argv.compiler} "                                                       \
                  f"{' '.join(compile_flags)} "                                             \
                  f"{' '.join(f'-I {include_path}'  for include_path in include_dirs)} "    \
                  f"{' '.join(f'-D {key}="{value}"' for key, value   in defines.items())} " \
                  f"-c {code_file} "                                                        \
                  f"-o {object_file}"
    elif compiler_id == "cl":
        command = f"{argv.compiler} "                                                       \
                  f"{' '.join(compile_flags)} "                                             \
                  f"{' '.join(f'/I {include_path}'  for include_path in include_dirs)} "    \
                  f"{' '.join(f'/D {key}="{value}"' for key, value   in defines.items())} " \
                  f"/c  {code_file} "                                                       \
                  f"/Fo {object_file}"
    compile_commands_logger.log(file=code_file, command=command.partition("&&")[0])
    await run(command, **run_args)
        
async def link_object(object_files, library_files, output_file, **run_args):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    command = ""
    if compiler_id == "g++" or compiler_id == "clang++":
        command = f"{argv.compiler} "           \
                  f"{' '.join(link_flags)} "    \
                  f"{' '.join(object_files)} "  \
                  f"{' '.join(library_files)} " \
                  f"-o {output_file}"
    elif compiler_id == "cl":
        command = f"{argv.compiler} "           \
                  f"{' '.join(link_flags)} "    \
                  f"{' '.join(object_files)} "  \
                  f"{' '.join(library_files)} " \
                  f"/Fe {output_file}"
    await run(command, **run_args)
    
async def run_executable(executable_file, **run_args):
    await run(f"./{executable_file}", **run_args)