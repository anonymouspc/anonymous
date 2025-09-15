from cppmake.basic.config          import config
from cppmake.logger.build_progress import build_progress_logger
from cppmake.system.all            import system
from cppmake.utility.algorithm     import recursive_search
from cppmake.utility.decorator     import context, deppkg, once, storetrue, trace, unique
from cppmake.utility.filesystem    import exist_dir, exist_file, iterate_dir
from cppmake.utility.scheduler     import scheduler
import asyncio
import importlib

@unique
class Package:
    @deppkg
    @once
    @trace
    async def new(self, name):
        from cppmake.target.module import Module
        self.name            = name
        self.build_dir       = f"./binary/{config.type}/package/{self.name}/build"
        self.install_dir     = f"./binary/{config.type}/package/{self.name}/install"
        self.include_dir     = f"./binary/{config.type}/package/{self.name}/install/include"
        self.library_dir     = f"./binary/{config.type}/package/{self.name}/install/lib"
        self.library_files   = [file for file in iterate_dir(self.library_dir, file_only=True) if file.endswith(system.static_suffix) or file.endswith(system.shared_suffix)] if exist_dir(self.library_dir) else []
        self.from_modules    = await asyncio.gather(*[...])
        self.import_packages = await asyncio.gather(*[recursive_search(from_module, navigate=lambda module: module.import_modules, collect=lambda module: module.import_package if module.import_package is not self else None) for from_module in self.from_modules])
        self.tool            = importlib.import_module(f"package.{self.name}")

    @context
    @once
    @trace
    async def build(self):
        if not self.is_built():
            await asyncio.gather(*[import_package.build() for import_package in self.import_packages])
            async with scheduler.schedule(scheduler.max):
                build_progress_logger.log("build package", self)
                await self.tool.build()
                self.library_files = [file for file in iterate_dir(self.library_dir, file_only=True) if file.endswith(system.static_suffix) or file.endswith(system.shared_suffix)] if exist_dir(self.library_dir) else []

    @storetrue
    def is_built(self):
        return False if config.update_package else exist_dir(self.install_dir)
    
    def exist(name):
        return exist_file(f"./tool/package/{name}.py")
    