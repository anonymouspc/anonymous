from common.config     import argv, compiler_id, compile_flags, link_flags, defines
from common.error      import LogicError
from common.filesystem import create_dir, parent_path
from common.logger     import compile_commands_logger, module_mapper_logger
from common.run        import run
import re

async def preprocess_file(code_file, name=None, module_file=None, **run_args):
    command = ""
    if compiler_id == "g++" or compiler_id == "clang++":
        command = [
            argv.compiler,
            *compile_flags,
            *[f"-D{key}={value}" for key, value in defines.items()],
            "-E", "-x", "c++", "-",
            "-o",              "-"
        ] 
    elif compiler_id == "cl":
        command = [
            argv.compiler,
            *[f"/D{key}={value}" for key, value in defines.items()]
        ]
    try:
        content = open(code_file, 'r').read()
        content = re.sub(r'^\s*#\s*include\s+(?!<version>).*$', "", content, flags=re.MULTILINE)
    except FileNotFoundError as e:
        raise LogicError(f"file {e.filename} not found")
    if name is not None and module_file is not None:
        module_mapper_logger.log(name=name, file=module_file)
    return await run(command=command, input_stdin=content, print_stdout=False, return_stdout=True, on_start=_print_preprocess_name(name) if argv.verbose else None, **run_args)
    
async def compile_module(code_file, include_dirs, module_file, object_file, **run_args):
    if compiler_id == "g++":
        commands = [[
            argv.compiler,
            *compile_flags,
            *[f"-I{include_dir}" for include_dir in include_dirs],
            *[f"-D{key}={value}" for key, value  in defines.items()],
            "-c", code_file,
            "-o", object_file
        ]]
    elif compiler_id == "clang++":
        commands = [
            [
                argv.compiler,
                *compile_flags,
                *[f"-I{include_dir}" for include_dir in include_dirs],
                *[f"-D{key}={value}" for key, value  in defines.items()],
                "--precompile", "-x", "c++-module", code_file,
                "-o",                               module_file
            ], 
            [
                argv.compiler,
                *compile_flags,
                "-c", module_file,
                "-o", object_file
            ]
        ]
    elif compiler_id == "cl":
        commands = [[
            argv.compiler,
            *compile_flags,
            *[f"/I{include_dir}" for include_dir in include_dirs],
            *[f"/D{key}={value}" for key, value  in defines.items()],
            "/c", "/interface", "/TP", code_file,
            "/ifcOutput",              module_file,
            "/Fo",                     object_file
        ]]
    compile_commands_logger.log(file=code_file, command=commands[0])
    await create_dir(parent_path(module_file))
    await create_dir(parent_path(object_file))
    for command in commands:
        await run(command=command, **run_args)

async def compile_source(code_file, include_dirs, object_file, **run_args):
    await create_dir(parent_path(object_file))
    if compiler_id == "g++" or compiler_id == "clang++":
        command = [
            argv.compiler,
            *compile_flags,
            *[f"-I{include_dir}" for include_dir in include_dirs],
            *[f"-D{key}={value}" for key, value  in defines.items()],
            "-c", code_file,
            "-o", object_file
        ]
    elif compiler_id == "cl":
        command = [
            argv.compiler,
            *compile_flags,
            *[f"/I{include_dir}" for include_dir in include_dirs],
            *[f"/D{key}={value}" for key, value  in defines.items()],
            "/c",  code_file,
            "/Fo", object_file
        ]
    compile_commands_logger.log(file=code_file, command=command)
    await create_dir(parent_path(object_file))
    await run(command=command, **run_args)
        
async def link_object(object_files, library_files, output_file, **run_args):
    if compiler_id == "g++" or compiler_id == "clang++":
        command = [
            argv.compiler,
            *link_flags,
            *object_files,
            *library_files,
            "-o", output_file
        ]
    elif compiler_id == "cl":
        command = [
            argv.compiler,
            *link_flags,
            *object_files,
            *library_files,
            "/Fe", output_file
        ]
    await create_dir(parent_path(output_file))
    await run(command=command, **run_args)
    
async def run_executable(executable_file, **run_args):
    await run(command=[f"./{executable_file}"], **run_args)



_printed_proprocess_name_count = 0
async def _print_preprocess_name(name):
    global _printed_proprocess_name_count
    _printed_proprocess_name_count += 1
    print(f"preprocess file [{_printed_proprocess_name_count}/n]: {name}")