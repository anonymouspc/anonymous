from .detail.version           import async_check_version
from cppmake.utility.decorator import member, syncable

@syncable
class Msvc:
    name          = "msvc"
    module_suffix = ".ixx"
    object_suffix = ".obj"
    async def async_init           (self, path="clang++"): ...
    async def async_preprocess_code(self, code_file,                                                                           defines={}): ...
    async def async_compile_module (self, code_file, module_file, object_file, module_dirs=[], include_dirs=[],                defines={}): ...
    async def async_compile_source (self, code_file, executable_file,          module_dirs=[], include_dirs=[], link_files=[], defines={}): ...


@member(Msvc)
async def async_init(self, path="cl.exe"):
    await async_check_version(command=[path], contains="msvc")
    self.path = path
    ...
    return self

    