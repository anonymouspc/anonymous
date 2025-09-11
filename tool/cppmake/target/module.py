from cppmake.basic.config               import config
from cppmake.compiler.all               import compiler
from cppmake.logger.build_progress      import build_progress_logger
from cppmake.logger.module_dependencies import module_dependencies_logger
from cppmake.logger.module_mappers      import module_mappers_logger
from cppmake.target.package             import Package
from cppmake.utility.algorithm          import recursive_search
from cppmake.utility.decorator          import context, depmod, once, storetrue, trace, unique
from cppmake.utility.filesystem         import exist_file, modified_time_of_file
from cppmake.utility.scheduler          import scheduler
import asyncio

@unique
class Module:
    @depmod
    @once
    @trace
    async def new(self, name):
        self.name           = name
        self.code_file      =                      f"./module/{self.name.replace('.', '/').replace(':', '/')}.cpp"
        self.module_file    = f"./binary/{config.type}/module/{self.name.replace('.', '.').replace(':', '-')}{compiler.module_suffix}"
        self.object_file    = f"./binary/{config.type}/module/{self.name.replace('.', '.').replace(':', '-')}{compiler.object_suffix}"
        self.import_modules = await asyncio.gather(*[Module(name) for name in await module_dependencies_logger.get(name=self.name, code_file=self.code_file)])
        self.import_package = await Package(name.partition('.')[0]) if Package.exist(name.partition('.')[0]) else None
        module_mappers_logger.log(name=self.name, module_file=self.module_file)

    @context
    @once
    @trace
    async def compile(self):
        if not self.is_compiled(): 
            await asyncio.gather(*[import_module.compile() for import_module in self.import_modules])
            await self.import_package.build() if self.import_package is not None else None
            async with scheduler.schedule():
                build_progress_logger.log("compile module", self)
                await compiler.compile_module(
                    code_file   =self.code_file,
                    module_file =self.module_file,
                    object_file =self.object_file,
                    include_dirs=await recursive_search(self, navigate=lambda module: module.import_modules, collect=lambda module: module.import_package.include_dir)
                )

    @storetrue
    def is_compiled(self):
        return (self.import_package.is_built() if self.import_package is not None else True)    and \
               all([module.is_compiled() for module in self.import_modules])                    and \
               exist_file(self.code_file)                                                       and \
               exist_file(self.module_file)                                                     and \
               exist_file(self.object_file)                                                     and \
               modified_time_of_file(self.code_file) <= modified_time_of_file(self.module_file) and \
               modified_time_of_file(self.code_file) <= modified_time_of_file(self.object_file)