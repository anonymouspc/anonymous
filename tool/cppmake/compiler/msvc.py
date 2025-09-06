from cppmake.basic.config    import config
from cppmake.utility.process import run_process, run_process_sync

class Msvc:
    name          = "msvc"
    module_suffix = ".ixx"
    object_suffix = ".obj"

    def __init__(self, path="g++"):
        self.path = path
        self.compile_flags = [
            "/std:c++latest",
            "/EHsc",
            "/W4",
            *(["/Od", "/Z7", "/DDEBUG" ] if config.type == "debug"   else
              ["/O2",        "/DNDEBUG"] if config.type == "release" else
              ["/O1"                   ] if config.type == "size"    else
              [])   
        ]
        self.link_flags = [
            "/MT"
        ]

    async def preprocess_file(self, code_file):
        pass

    async def compile_module(self, code_file, module_file, object_file, include_dirs, module_only=False):
        pass

    async def compile_source(self, output, code_file, output_file, include_dirs, object_files, library_files):
        pass

    def check(path):
        return run_process_sync(command=[path], return_stdout=True).startswith("Microsoft")