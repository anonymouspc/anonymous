from cppmake.basic.config          import config
from cppmake.compiler.all          import compiler
from cppmake.execution.operation   import when_all
from cppmake.logger.module_mappers import module_mappers_logger
from cppmake.logger.unit_imports   import unit_imports_logger
from cppmake.unit.package          import Package
from cppmake.utility.algorithm     import recursive_collect
from cppmake.utility.filesystem    import parent_path, exist_file, modified_time_of_file
from cppmake.utility.decorator     import member, namable, once, syncable, trace, unique

@unique
class Module:
    def           __init__        (self, *args, **kwargs): ... # provide one of 'name' or 'file'
    async def     __ainit__       (self, *args, **kwargs): ... # provide one of 'name' or 'file'
    def             precompile    (self):             ...
    async def async_precompile    (self):             ...
    def             is_precompiled(self):             ...
    async def async_is_precompiled(self):             ...
    def             name_to_file  (name):             ...
    def             file_to_name  (file):             ...



@member(Module)
@syncable
@namable
@trace
async def __ainit__(self, name):
    self.name           = name
    self.code_file      =                                     f"module/{self.name.replace('.', '/').replace(':', '/')}.cpp" if not Package.exist(self.name.split('.')[0]) else \
                          f"./package/{self.name.split('.')[0]}/module/{self.name.replace('.', '/').replace(':', '/')}.cpp"
    self.module_file    =                f"binary/{config.type}/module/{self.name.replace('.', '/').replace(':', '-')}{compiler.module_suffix}"
    self.object_file    =                f"binary/{config.type}/module/{self.name.replace('.', '/').replace(':', '-')}{compiler.object_suffix}"
    self.import_modules = await unit_imports_logger.async_get_imports(self)
    self.import_package = await Package.__anew__(self.name.split('.')[0]) if Package.exist(self.name.split('.')[0]) else None
    module_mappers_logger.log_mapper(module=self)

@member(Module)
@syncable
@once
@trace
async def async_precompile(self):
    if not await self.async_is_precompiled():
        await when_all([module.async_precompile() for module in self.import_modules])
        await self.import_package.async_make() if self.import_package is not None else None
        await compiler.async_precompile(
            code_file   =self.code_file,
            module_file =self.module_file,
            object_file =self.object_file,
            module_dirs =recursive_collect(self, next=lambda module: module.import_modules, collect=lambda module: parent_path(module.module_file),   on_root=True),
            include_dirs=recursive_collect(self, next=lambda module: module.import_modules, collect=lambda module: module.import_package.include_dir, on_root=True)
        )

@member(Module)
@syncable
@once
async def async_is_precompiled(self):
    return await when_all([module.async_is_precompiled() for module in self.import_modules])        and \
           (await self.import_package.async_is_made() if self.import_package is not None else True) and \
           exist_file(self.code_file)                                                               and \
           exist_file(self.module_file)                                                             and \
           exist_file(self.object_file)                                                             and \
           modified_time_of_file(self.code_file) <= modified_time_of_file(self.module_file)         and \
           modified_time_of_file(self.code_file) <= modified_time_of_file(self.object_file)

@member(Module)
def name_to_file(name):
    return                                f"module/{name.replace('.', '/').replace(':', '/')}.cpp" if not Package.exist(name.split('.')[0]) else \
           f"./package/{name.split('.')[0]}/module/{name.replace('.', '/').replace(':', '/')}.cpp"

@member(Module)
def file_to_name(file):
    return file.partition("module/")[2].removesuffix(".cpp").replace('/', '.')