from cppmake.basic.config             import argv
from cppmake.basic.system             import object_suffix
from cppmake.compiler.compiler        import compiler
from cppmake.logger.dependency_logger import dependency_logger
from cppmake.target.module            import Module
from cppmake.utility.once             import once
import asyncio

class Source:
    pool = {}

    async def __new__(self, name):
        if name in Source.pool.keys():
            self = Source.pool[name]  
        else:
            self = super().__new__(self)
            Source.pool[name] = self

            self.name            = name
            self.code_file       =                 f"./source/{self.name.replace('.', '/').replace(':', '/')}.cpp"
            self.output_prefix   = f"./bin/{argv.type}/source/{self.name.replace('.', '/').replace(':', '/')}"
            self.import_modules  = await asyncio.gather(Module(name=name) for name in await dependency_logger.get(name=self.name))



        return self
    
    @asyncio.create_task
    async def compile(self, target="executable"):
        self.is_compiled = all([                                                                 
            module.is_compiled for module in self.import_modules,
            await exist_file(self.code_file),
            await exist_file(self.object_file),
            await getmtime_file(self.code_file) <= await getmtime_file(self.object_file)
        ])
        await asyncio.gather(import_module.compile() for import_module in self.import_modules)
        await compiler.compile_source(
            code_file   =self.code_file,
            include_dirs=self.include_dirs,
            output_file =f"{self.output_prefix}.{globals()[f"{target}_suffix"]}",
        )

        