from cppmake.basic.config          import config
from cppmake.compiler.all          import compiler
from cppmake.execution.operation   import when_all
from cppmake.file.file_system      import parent_path, exist_file, modified_time_of_file
from cppmake.logger.module_imports import module_imports_logger
from cppmake.logger.module_mappers import module_mappers_logger
from cppmake.unit.package          import Package
from cppmake.utility.algorithm     import recursive_collect
from cppmake.utility.decorator     import member, once, syncable, trace, unique

@unique
class Module:
    def           __init__        (self, name): ...
    async def     __ainit__       (self, name): ... 
    def             precompile    (self):       ...
    async def async_precompile    (self):       ...
    def             is_precompiled(self):       ...
    async def async_is_precompiled(self):       ...



@member(Module)
@syncable
@trace
async def __ainit__(self, name):
    self.name           = name
    self.code_file      =                                                   f"module/{self.name.replace('.', '/').replace(':', '/')}.cpp" if not Package.exist(self.name.split(':')[0].split('.')[0]) else \
                          f"./package/{self.name.split(':')[0].split('.')[0]}/module/{self.name.replace('.', '/').replace(':', '/')}.cpp"
    self.module_file    =                              f"binary/{config.type}/module/{self.name.replace('.', '/').replace(':', '-')}{compiler.module_suffix}"
    self.object_file    =                              f"binary/{config.type}/module/{self.name.replace('.', '/').replace(':', '-')}{compiler.object_suffix}"
    self.import_modules = await when_all([Module.__anew__(name) for name in await module_imports_logger.async_get_imports(self)])
    self.import_package = await Package.__anew__(self.name.split(':')[0].split('.')[0]) if Package.exist(self.name.split(':')[0].split('.')[0]) else None
    module_mappers_logger.log_mapper(self)

@member(Module)
@syncable
@once
@trace
async def async_precompile(self):
    if not await self.async_is_precompiled():
        await when_all([module.async_precompile() for module in self.import_modules])
        await self.import_package.async_build() if self.import_package is not None else None
        await compiler.async_precompile(
            code_file   =self.code_file,
            module_file =self.module_file,
            object_file =self.object_file,
            module_dirs =recursive_collect(self, next=lambda module: module.import_modules, collect=lambda module: parent_path(module.module_file)),
            include_dirs=recursive_collect(self, next=lambda module: module.import_modules, collect=lambda module: module.import_package.include_dir)
        )

@member(Module)
@syncable
@once
async def async_is_precompiled(self):
    return all(await when_all([module.async_is_precompiled() for module in self.import_modules]))    and \
           (await self.import_package.async_is_built() if self.import_package is not None else True) and \
           exist_file(self.code_file)                                                                and \
           exist_file(self.module_file)                                                              and \
           exist_file(self.object_file)                                                              and \
           modified_time_of_file(self.code_file) <= modified_time_of_file(self.module_file)          and \
           modified_time_of_file(self.code_file) <= modified_time_of_file(self.object_file)