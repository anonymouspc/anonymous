from .detail.version               import async_check_version
from cppmake.basic.config          import config
from cppmake.execution.run         import async_run
from cppmake.logger.module_mappers import module_mappers_logger
from cppmake.utility.decorator     import member, syncable
from cppmake.utility.filesystem    import parent_path, create_dir

@syncable
class Gcc:
    name          = "gcc"
    module_suffix = ".gcm"
    object_suffix = ".o"
    async def async_init           (self, path="clang++"): ...
    async def async_preprocess_code(self, code_file,                                                                           defines={}): ...
    async def async_compile_module (self, code_file, module_file, object_file, module_dirs=[], include_dirs=[],                defines={}): ...
    async def async_compile_source (self, code_file, executable_file,          module_dirs=[], include_dirs=[], link_files=[], defines={}): ...



@member(Gcc)
async def async_init(self, path="g++"):
    await async_check_version(command=[path, "--version"], contains="gcc")
    self.path = path
    self.compile_flags = [
       f"-std={config.standard}", "-fmodules", 
        "-fdiagnostics-colors=always", "-fdiagnostics-format=sarif-stderr",
        "-Wall", "-Wno-global-module", "-Wno-deprecated-variadic-comma-omission",
     *(["-O0", "-g", "-DDEBUG", "-fno-inline"] if config.type == "debug"   else
       ["-O3",       "-DNDEBUG"              ] if config.type == "release" else
       ["-Os"                                ] if config.type == "size"    else 
       []) 
    ]
    self.link_flags = [
        "-lstdc++exp",
     *(["-s"] if config.type == "release" or config.type == "size" else 
       [])
    ]
    return self

@member(Gcc)
async def async_preprocess_code(self, code_file, defines={}):
    return await async_run(
        command=[
            self.path,
           *self.compile_flags,
           *[f"-D{key}={value}" for key, value in defines.items()],
            "-E", code_file,
            "-o", "-"
        ],
        print_stdout=False,
        return_stdout=True
    )

@member(Gcc)
async def async_compile_module(self, code_file, module_file, object_file, module_dirs=[], include_dirs=[], defines={}):
    create_dir(parent_path(module_file))
    create_dir(parent_path(object_file))
    await async_run(
        command=[
            self.path,
           *self.compile_flags,
           *[f"-fmodule-mapper={module_mappers_logger.get(module_dir)}" for module_dir  in module_dirs    ],
           *[f"-I{include_dir}"                                         for include_dir in include_dirs   ],
           *[f"-D{key}={value}"                                         for key, value  in defines.items()],
            "-c", code_file,
            "-o", object_file
        ],
        log_command=(True, code_file),
        log_stderr =True
    )

@member(Gcc)
async def async_compile_source(self, code_file, executable_file, include_dirs=[], module_dirs=[], link_files=[], defines={}):
    create_dir(parent_path(executable_file))
    await async_run(
        command=[
            self.path,
           *self.compile_flags,
           *[f"-fmodule-mapper={module_mappers_logger.get(module_dir)}" for module_dir  in module_dirs    ],
           *[f"-I{include_dir}"                                         for include_dir in include_dirs   ],
           *[f"-D{key}={value}"                                         for key, value  in defines.items()],
            code_file,
           *self.link_flags,
           *link_files,
            "-o", executable_file
        ],
        log_command=(True, code_file),
        log_stderr =True
    )
