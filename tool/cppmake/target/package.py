from cppmake.basic.config          import config
from cppmake.logger.build_progress import build_progress_logger
from cppmake.system.all            import system
from cppmake.utility.decorator     import context, once, trace, unique
from cppmake.utility.filesystem    import exist_dir, iterate_dir
from cppmake.utility.scheduler     import scheduler
import importlib

@unique
class Package:
    @once
    @trace
    async def new(self, name):
        self.name          = name
        self.build_dir     = f"./bin/{config.type}/package/{self.name}/build"
        self.install_dir   = f"./bin/{config.type}/package/{self.name}/install"
        self.include_dir   = f"./bin/{config.type}/package/{self.name}/install/include"
        self.library_dir   = f"./bin/{config.type}/pacakge/{self.name}/install/lib"
        self.library_files = [file for file in iterate_dir(self.library_dir, file_only=True) if file.endswith(system.static_suffix) or file.endswith(system.shared_suffix)] if exist_dir(self.library_dir) else []
        self.tool          = importlib.import_module(f"package.{self.name}")

    @context
    @once
    @trace
    async def build(self):
        if not self.is_built():
            async with scheduler.schedule(scheduler.max):
                build_progress_logger.log("build package", self)
                await self.tool.build()
                self.library_files = [file for file in iterate_dir(self.library_dir, file_only=True) if file.endswith(system.static_suffix) or file.endswith(system.shared_suffix)] if exist_dir(self.library_dir) else []

    def is_built(self):
        # todo: optimize with cache
        return False if config.update_package else exist_dir(self.install_dir)
    
    def exist(name):
        return exist_dir(f"./package/{name}")
    