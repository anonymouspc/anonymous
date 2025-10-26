from cppmake.basic.config       import config
from cppmake.basic.define       import define
from cppmake.basic.keyword      import keyword
from cppmake.error.process      import ProcessError
from cppmake.utility.process    import run_process, run_process_sync
from cppmake.utility.filesystem import parent_path, create_dir

class Gcc:
    name          = "gcc"
    module_suffix = ".gcm"
    object_suffix = ".o"

    def __init__(self, path="g++"):
        self.path = path
        self.compile_flags = [
            "-std=c++26", 
            "-Wall",
            "-fdiagnostics-color=always",
            "-fmodules",
            "-fmodule-mapper=./binary/cache/module_mappers.txt",
            "-Wno-global-module",
            "-Wno-deprecated-variadic-comma-omission",
            *(["-O0", "-g", "-DDEBUG", "-fno-inline"] if config.type == "debug"   else
              ["-O3",       "-DNDEBUG"              ] if config.type == "release" else
              ["-Os"                                ] if config.type == "size"    else 
              []) 
        ]
        self.link_flags = [
            "-fuse-ld=lld",
            "-lstdc++exp",
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

    async def compile_module(self, code_file, module_file, object_file, include_dirs, with_keyword=True):
        create_dir(parent_path(module_file))
        create_dir(parent_path(object_file))
        await run_process(
            command=[
                self.path,
                *self.compile_flags,
                * [f"-I{include_dir}" for include_dir in include_dirs  ],
                * [f"-D{key}={value}" for key, value  in define .items()],
                *([f"-D{key}={value}" for key, value  in keyword.items()] if with_keyword else []),
                "-c", code_file,
                "-o", object_file
            ],
            log_command=(True, code_file)
        )

    async def compile_source(self, code_file, executable_file, include_dirs, link_files, with_keyword=True):
        create_dir(parent_path(executable_file))
        await run_process(
            command=[
                self.path,
                *self.compile_flags,
                * [f"-I{include_dir}" for include_dir in include_dirs  ],
                * [f"-D{key}={value}" for key, value  in define .items()],
                *([f"-D{key}={value}" for key, value  in keyword.items()] if with_keyword else []),
                code_file,
                *self.link_flags,
                *link_files
                "-o", executable_file
            ],
            log_command=(True, code_file)
        )

    def check(path):
        try:
            return "gcc" in run_process_sync(command=[path, "--version"], return_stdout=True).lower()
        except ProcessError:
            return False