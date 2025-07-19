from common.algorithm import recursive_find
from common.compiler  import preprocess_file, compile_source
from common.config    import type, object_suffix
from common.error     import BuildError
from common.lazy      import Lazy
from common.scheduler import scheduler
from file.module      import Module
from file.package     import Package
import asyncio
import os
import re
  
class Source:
    pool    = {}
    current = 0
    total   = 0

    async def __new__(self, name):
        try:
            if name in Source.pool.keys():
                self = Source.pool[name]
            else:
                self = super().__new__(self)
                Source.pool[name] = self
                self.new_task = Lazy(self._create_new_task(name=name))
            return await self.new_task
        except BuildError as e:
            raise BuildError(f"In source {self.name}:\n{e}")

    async def compile(self):
        try:
            if not self.is_compiled:
                if self.compile_task is None:
                    self.compile_task = Lazy(self._create_compile_task())
                await self.compile_task
        except BuildError as e:
            raise BuildError(f"In source {self.name}:\n{e}")

    def __eq__(self, str):
        return self.name == str

    async def _create_new_task(self, name):
        # Info
        self.name        = name
        self.code_file   =            f"./source/{self.name.replace('.', '/').replace(':', '/')}.cpp"
        self.object_file = f"./bin/{type}/source/{self.name.replace('.', '.').replace(':', '-')}.{object_suffix}"
        async with scheduler.schedule():
            self.content = await preprocess_file(code_file=self.code_file)

        # Import
        import_tasks = []
        import_names = re.findall(r'^\s*import\s+([\w\.:]+)\s*;\s*$', self.content, flags=re.MULTILINE)
        for import_name in import_names:
            import_tasks += [Module(import_name)]
        self.import_modules = await asyncio.gather(*import_tasks)

        # Status
        self.is_compiled = all(module.is_compiled for module in self.import_modules)              and \
                           os.path.isfile(self.code_file)                                         and \
                           os.path.isfile(self.object_file)                                       and \
                           os.path.getmtime(self.code_file) <= os.path.getmtime(self.object_file)
        if not self.is_compiled:
            self.compile_task = None
            Source.total += 1

        # Return
        return self

    async def _create_compile_task(self):
        # Import
        depend_tasks = []
        for import_module in self.import_modules:
            depend_tasks += [import_module.compile()]
        await asyncio.gather(*depend_tasks)

        # Self
        async with scheduler.schedule():
            Source.current += 1
            print(f"compile source [{Source.current}/{Source.total}]: {self.name}")
            await compile_source(code_file   =self.code_file, 
                                 include_dirs=await recursive_find(node=self, func=Source._module_to_include_dir, root=False),
                                 object_file =self.object_file)
        
        # Status
        self.is_compiled = True

    async def _module_to_include_dir(module):
        return (await Package(module.name)).include_dir if await Package.exist(module.name) else None
