from cppmake.basic.config       import config
from cppmake.basic.define       import define
from cppmake.utility.filesystem import parent_path, create_dir
from cppmake.utility.process    import run_process, run_process_sync

class Clang:
    name          = "clang"
    module_suffix = ".pcm"
    object_suffix = ".o"

    def __init__(self, path="clang++"):
        self.path = path
        self.compile_flags = [
            "-std=c++26", 
            "-Wall", 
            "-fdiagnostics-color=always",
           f"-fprebuilt-module-path=./binary/{config.type}/module",
            "-Wno-reserved-module-identifier",
            "-Wno-deprecated-missing-comma-variadic-parameter",
            *(["-O0", "-g", "-DDEBUG", "-fno-inline"] if config.type == "debug"   else
              ["-O3",       "-DNDEBUG"              ] if config.type == "release" else
              ["-Os"                                ] if config.type == "size"    else 
              [])
        ]
        self.link_flags = [
            "-w",
            *(["-s"] if config.type == "release" or config.type == "size" else [])
        ]

    async def preprocess_code(self, code):
        return await run_process(
            command=[
                self.path,
                *self.compile_flags,
                *[f"-D{key}={value}" for key, value in define.items()],
                "-E", "-x", "c++", "-",
                "-o",              "-"
            ],
            input_stdin=code,
            print_stdout=False,
            return_stdout=True
        )

    async def compile_module(self, code_file, module_file, object_file, include_dirs, module_only=False):
        create_dir(parent_path(module_file))
        create_dir(parent_path(object_file))
        await run_process(
            command=[
                self.path,
                *self.compile_flags,
                *[f"-I{include_dir}" for include_dir in include_dirs  ],
                *[f"-D{key}={value}" for key, value  in define.items()],
                "--precompile", "-x", "c++-module", code_file,
                "-o",                               module_file,
            ],
            log_command=(True, code_file)
        )
        if not module_only:
            await run_process(
                command=[
                    self.path,
                    *self.compile_flags,
                    "-c", module_file,
                    "-o", object_file
                ]
            )

    async def compile_source(self, output, code_file, output_file, include_dirs, object_files, library_files):
        create_dir(parent_path(output_file))
        await run_process(
            command=[
                self.path,
                *self.compile_flags,
                *[f"-I{include_dir}" for include_dir in include_dirs  ],
                *[f"-D{key}={value}" for key, value  in define.items()],
                code_file,
                *self.link_flags,
                *(["-shared", "-fPIC"] if output == "shared" else []),
                *object_files,
                *library_files,
                "-o", output_file
            ],
            log_command=(True, code_file)
        )

    def check(path):
        return run_process_sync(command=[path, "--version"], return_stdout=True).startswith("clang++")