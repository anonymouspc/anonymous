from cppmake.basic.config          import config
from cppmake.logger.build_progress import build_progress_logger
from cppmake.system.all            import system
from cppmake.utility.algorithm     import recursive_search
from cppmake.utility.algorithm     import recursive_search
from cppmake.utility.decorator     import once, storetrue, trace, unique
from cppmake.utility.filesystem    import exist_dir, exist_file, iterate_dir
from cppmake.utility.scheduler     import scheduler
import asyncio
import importlib

@unique
class Package:
    @once
    @trace
    async def new(self, name):
        from cppmake.target.module import Module
        assert Package.exist(name)
        self.name            = name
        self.install_dir     = f"./binary/{config.type}/package/{self.name}/install"
        self.include_dir     = f"./binary/{config.type}/package/{self.name}/install/include"
        self.library_dir     = f"./binary/{config.type}/package/{self.name}/install/lib"
        self.from_modules    = await asyncio.gather()
        self.import_packages = recursive_search(await Module(self.name), navigate=lambda module: module.import_modules, collect=lambda module: module.import_package, root=False)
        self.tool            = importlib.util.module_from_spec(importlib.util.spec_from_file_location(name=f"package.{self.name}.tool.build", location=f"./package/{self.name}/tool/build.py"))

    @once
    @trace
    async def build(self):
        if not self.is_built():
            await asyncio.gather(*[import_package.build() for import_package in self.import_packages])
            async with scheduler.schedule(scheduler.max):
                await self.tool.build()
                self.library_files = [file for file in iterate_dir(self.library_dir, file_only=True) if file.endswith(system.static_suffix) or file.endswith(system.shared_suffix)] if exist_dir(self.library_dir) else []

    @storetrue
    def is_built(self):
        return False if config.update_package else exist_dir(self.install_dir)
    
    def exist(name):
        return exist_dir(f"./package/{name}")
    
    ##### private #####
    async def _find_modules(self):
        for file in iterate_dir(f"./package/{self/name}")
    