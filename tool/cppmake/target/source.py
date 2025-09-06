from cppmake.basic.config               import config
from cppmake.compiler.all               import compiler
from cppmake.logger.build_progress      import build_progress_logger
from cppmake.logger.module_dependencies import module_dependencies_logger
from cppmake.system.all                 import system
from cppmake.target.module              import Module
from cppmake.utility.algorithm          import recursive_find
from cppmake.utility.decorator          import context, once, trace, unique
from cppmake.utility.filesystem         import exist_file, modified_time_of_file
from cppmake.utility.scheduler          import scheduler
import asyncio

@unique
class Source:
    @once
    @trace
    async def new(self, name):
        self.name           = name
        self.code_file      =                   f"./source/{self.name.replace('.', '/')}.cpp"
        self.output_prefix  = f"./bin/{config.type}/source/{self.name.replace('.', '.')}"
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
                    include_dirs =await recursive_find(self, navigates=["import_modules", "import_package"], target="include_dir"),
                    object_files =await recursive_find(self, navigates=["import_modules", "import_pacakge"], target="object_file"),
                    library_files=await recursive_find(self, navigates=["import_modules", "import_package"], target="library_files", flatten=True)
                )

    def is_compiled(self, output="executable"):
        # todo: optimize with cache
        output_file = f"{self.output_prefix}{getattr(system, f"{output}_suffix")}"
        return all([module.is_compiled() for module in self.import_modules])               and \
               exist_file(self.code_file)                                                  and \
               exist_file(output_file)                                                     and \
               modified_time_of_file(self.code_file) <= modified_time_of_file(output_file)