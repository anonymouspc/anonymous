from common.algorithm import recursive_find
from common.compiler  import preprocess_file, compile_source
from common.config    import argv, object_suffix
from common.error     import LogicError
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
        if name in Source.pool.keys():
            self = Source.pool[name]
        else:
            self = super().__new__(self)
            Source.pool[name] = self
            self.new_task = asyncio.create_task(self._create_new_task(name=name))
        await self.new_task
        return self

    async def compile(self):
        if not self.is_compiled:
            if self.compile_task is None:
                self.compile_task = asyncio.create_task(self._create_compile_task())
            await self.compile_task

    def __eq__(self, str):
        return self.name == str

    async def _create_new_task(self, name):
        try:
            # Info
            self.name        = name
            self.code_file   =            f"./source/{self.name.replace('.', '/').replace(':', '/')}.cpp"
            self.object_file = f"./bin/{argv.type}/source/{self.name.replace('.', '.').replace(':', '-')}.{object_suffix}"
            self.content     = await preprocess_file(code_file=self.code_file)

            # Import
            import_names = re.findall(r'^\s*import\s+([\w\.:]+)\s*;\s*$', self.content, flags=re.MULTILINE)
            self.import_modules = await asyncio.gather(*[Module(import_name) for import_name in import_names])

            # Status
            self.is_compiled = all(module.is_compiled for module in self.import_modules)              and \
                               os.path.isfile(self.code_file)                                         and \
                               os.path.isfile(self.object_file)                                       and \
                               os.path.getmtime(self.code_file) <= os.path.getmtime(self.object_file)
            if not self.is_compiled:
                self.compile_task = None
                Source.total += 1
            
        except LogicError as e:
            raise e.add_prefix(f"In source {self.name}:")

    async def _create_compile_task(self):
        try:
            # Import
            await asyncio.gather(*[import_module.compile() for import_module in self.import_modules])

            # Self
            await compile_source(code_file   =self.code_file, 
                                 include_dirs=await recursive_find(node=self, func=Source._module_to_include_dir, root=False),
                                 object_file =self.object_file,
                                 on_start    =Source._print_progress(name=self.name))
            
            # Status
            self.is_compiled = True

        except LogicError as e:
            raise e.add_prefix(f"In source {self.name}:")

    async def _module_to_include_dir(module):
        return (await Package(module.name)).include_dir if await Package.exist(module.name) else None
    
    async def _print_progress(name):
        Source.current += 1
        print(f"compile source [{Source.current}/{Source.total}]: {name}")
