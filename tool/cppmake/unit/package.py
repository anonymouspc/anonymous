from cppmake.basic.config          import config
from cppmake.execution.operation   import when_all
from cppmake.execution.scheduler   import scheduler
from cppmake.logger.package_status import package_status_logger
from cppmake.logger.unit_imports   import unit_imports_logger
from cppmake.utility.algorithm     import async_recursive_collect
from cppmake.utility.decorator     import member, namable, once, syncable, trace, unique
from cppmake.utility.filesystem    import exist_dir, iterate_dir
import importlib

@unique
class Package:
    def           __init__     (self, *args, **kwargs): ... # provide one of 'name' or 'dir'
    async def     __ainit__    (self, *args, **kwargs): ... # provide one of 'name' or 'dir'
    def             make       (self):       ...
    async def async_make       (self):       ...
    def             is_made    (self):       ...
    async def async_is_made    (self):       ...
    def             exist      (name):       ...
    def             name_to_dir(name):       ...
    def             dir_to_name(dir ):       ...



@member(Package)
@syncable
@namable
@trace
async def __ainit__(self, name):
    from cppmake.unit.module import Module
    self.name            = name
    self.package_dir     = f"package/{self.name}"
    self.git_dir         = f"package/{self.name}/git"
    self.module_dir      = f"package/{self.name}/module"
    self.tool_dir        = f"package/{self.name}/tool"
    self.build_dir       = f"binary/{config.type}/package/{self.name}/build"
    self.install_dir     = f"binary/{config.type}/package/{self.name}/install"
    self.include_dir     = f"binary/{config.type}/package/{self.name}/install/include"
    self.lib_dir         = f"binary/{config.type}/package/{self.name}/install/lib"
    self.import_packages = await when_all([async_recursive_collect(Module.file_to_name(file), next=lambda name: unit_imports_logger.async_peek_imports(name), collect=lambda name: Package.__anew__(name.split('.')[0]) if name != self.name and Package.exist(name) else None, on_root=False) for file in iterate_dir(self.module_dir)])
    self.tool            = importlib.machinery.SourceFileLoader(fullname=f"package.{self.name}.tool.cppmake", path=f"package/{self.name}/tool/cppmake.py").load_module()

@member(Package)
@syncable
@once
@trace
async def async_make(self):
    if not await self.async_is_made():
        await when_all([package.async_make() for package in self.import_packages])
        async with scheduler.schedule(scheduler.max):
            self.tool.configure() if hasattr(self.tool, "configure") else None
            self.tool.build    () if hasattr(self.tool, "build"    ) else None
            self.tool.install  () if hasattr(self.tool, "install"  ) else None
            await package_status_logger.async_log_status(self)

@member(Package)
@syncable
@once
async def async_is_made(self):
    return exist_dir(self.install_dir) and \
           await package_status_logger.async_get_status(self)

@member(Package)
def exist(name):
    return exist_dir(f"package/{name}")

@member(Package)
def name_to_dir(name):
    return f"package/{name}"

@member(Package)
def dir_to_name(dir):
    return dir.removeprefix("package/")

    