from cppmake.basic.config          import config
from cppmake.execution.operation   import when_all
from cppmake.execution.scheduler   import scheduler
from cppmake.file.file_import      import import_file
from cppmake.file.file_system      import exist_dir, iterate_dir
from cppmake.logger.package_status import package_status_logger
from cppmake.utility.algorithm     import recursive_collect
from cppmake.utility.decorator     import member, once, syncable, trace, unique

@unique
class Package:
    def           __init__  (self, name): ...
    async def     __ainit__ (self, name): ...
    def             build   (self):       ...
    async def async_build   (self):       ...
    def             is_built(self):       ...
    async def async_is_built(self):       ...
    def             exist   (      name): ...



@member(Package)
@syncable
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
  # self.modules         = await when_all([Module.__anew__(file.removeprefix(f"{self.module_dir}/").removesuffix(".cpp").replace('/', '.')) for file in iterate_dir(self.module_dir)])
  # self.import_packages = recursive_collect(self.modules, next=lambda module: module.import_modules, collect=lambda module: module.import_package if module.import_package is not self else None)
    self.tool            = import_file(f"package/{self.name}/tool/cppmake.py")

@member(Package)
@syncable
@once
@trace
async def async_build(self):
    if not await self.async_is_built():
      # await when_all([package.async_build() for package in self.import_packages])
        async with scheduler.schedule(scheduler.max):
            self.tool.build() if hasattr(self.tool, "build") else None
            await package_status_logger.async_log_status(self)

@member(Package)
@syncable
@once
async def async_is_built(self):
  # return all(await when_all([package.async_is_built() for package in self.import_packages])) and
    return exist_dir(self.install_dir)                                                         and \
           await package_status_logger.async_get_status(self)

@member(Package)
def exist(name):
    return exist_dir(f"package/{name}")

    