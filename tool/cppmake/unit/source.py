from cppmake.basic.config          import config
from cppmake.compiler.all          import compiler
from cppmake.execution.operation   import when_all
from cppmake.execution.scheduler   import scheduler
from cppmake.file.file_system      import parent_path, exist_file, modified_time_of_file, iterate_dir
from cppmake.logger.module_imports import module_imports_logger
from cppmake.system.all            import system
from cppmake.unit.module           import Module
from cppmake.utility.algorithm     import recursive_collect
from cppmake.utility.decorator     import member, once, syncable, trace, unique

@unique
class Source:
    def           __init__      (self, name): ...
    async def     __ainit__     (self, name): ...
    def             compile     (self):       ...
    async def async_compile     (self):       ...
    def             is_compiled (self):       ...
    async def async_is_compiled (self):       ...



@member(Source)
@syncable
@trace
async def __ainit__(self, name):
    self.name            = name
    self.code_file       =                      f"source/{self.name.replace('.', '/')}.cpp"
    self.executable_file = f"binary/{config.type}/source/{self.name.replace('.', '.')}{system.executable_suffix}"
    self.import_modules  = await when_all([Module.__anew__(name) for name in await module_imports_logger.async_get_imports(self)])

@member(Source)
@syncable
@once
@trace
async def async_compile(self):
    if not await self.async_is_compiled():
        await when_all([module.async_precompile() for module in self.import_modules])
        async with scheduler.schedule():
            await compiler.async_compile(
                code_file      =self.code_file,
                executable_file=self.executable_file,
                module_dirs    =recursive_collect(self, next=lambda module: module.import_modules, collect=lambda module: parent_path(module.module_file),                            root=False),
                include_dirs   =recursive_collect(self, next=lambda module: module.import_modules, collect=lambda module: module.import_package.include_dir,                          root=False),
                link_files     =recursive_collect(self, next=lambda module: module.import_modules, collect=lambda module: module.object_file,                                         root=False) + 
                                recursive_collect(self, next=lambda module: module.import_modules, collect=lambda module: iterate_dir(module.import_package.lib_dir, file_only=True), root=False, flatten=True)
            )

@member(Source)
@syncable
@once
async def async_is_compiled(self):
    return all(await when_all([module.async_is_precompiled() for module in self.import_modules])) and \
           exist_file(self.code_file)                                                             and \
           exist_file(self.executable_file)                                                       and \
           modified_time_of_file(self.code_file) <= modified_time_of_file(self.executable_file)