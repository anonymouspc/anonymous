from cppmake.basic.config               import config
from cppmake.compiler.all               import compiler
from cppmake.logger.build_progress      import build_progress_logger
from cppmake.logger.module_dependencies import module_dependencies_logger
from cppmake.system.all                 import system
from cppmake.target.module              import Module
from cppmake.utility.algorithm          import recursive_search
from cppmake.utility.decorator          import context, once, storetrue, trace, unique
from cppmake.utility.filesystem         import exist_file, modified_time_of_file
from cppmake.utility.scheduler          import scheduler
import asyncio

@unique
class Source:
    @once
    @trace
    async def new(self, name):
        self.name           = name
        self.code_file      =                      f"./source/{self.name.replace('.', '/')}.cpp"
        self.output_prefix  = f"./binary/{config.type}/source/{self.name.replace('.', '.')}"
        self.import_modules = await asyncio.gather(*[Module(name) for name in await module_dependencies_logger.get(name=self.name, code_file=self.code_file)])

    @context
    @once
    @trace
    async def compile(self, output="executable"):
        output_file = f"{self.output_prefix}{getattr(system, f"{output}_suffix")}"
        if not self.is_compiled():
            await asyncio.gather(*[import_module.compile() for import_module in self.import_modules])
            async with scheduler.schedule():
                build_progress_logger.log("compile source", self)
                await compiler.compile_source(
                    output       =output,
                    code_file    =self.code_file,
                    output_file  =output_file,
                    include_dirs =await recursive_search(self, navigate=lambda module: module.import_modules, collect=lambda module: module.import_package.include_dir,   root=False),
                    object_files =await recursive_search(self, navigate=lambda module: module.import_modules, collect=lambda module: module.object_file,                  root=False),
                    library_files=await recursive_search(self, navigate=lambda module: module.import_modules, collect=lambda module: module.import_package.library_files, root=False, flatten=True)
                )

    @storetrue
    def is_compiled(self, output="executable"):
        # todo: optimize with cache
        output_file = f"{self.output_prefix}{getattr(system, f"{output}_suffix")}"
        return all([module.is_compiled() for module in self.import_modules])               and \
               exist_file(self.code_file)                                                  and \
               exist_file(output_file)                                                     and \
               modified_time_of_file(self.code_file) <= modified_time_of_file(output_file)