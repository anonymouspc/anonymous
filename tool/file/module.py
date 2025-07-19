from common.algorithm import recursive_find
from common.config    import type, module_suffix, object_suffix
from common.compiler  import preprocess_file, compile_module
from common.error     import BuildError
from common.lazy      import Lazy
from common.scheduler import scheduler
from file.package     import Package
import asyncio
import os
import re

class Module:
    pool    = {}
    current = 0
    total   = 0

    async def __new__(self, name, from_modules=[]):
        try:
            if name in Module.pool.keys():
                self = Module.pool[name]
            else:
                self = super().__new__(self)
                Module.pool[name] = self
                self.new_task = Lazy(self._create_new_task(name=name, from_modules=from_modules))
            return await self.new_task
        except BuildError as e:
            raise BuildError(f"In module {self.name}:\n{e}")

    async def compile(self):
        print(f"{self.name}.compile()")
        try:
            if not self.is_compiled:
                if self.compile_task is None:
                    self.compile_task = Lazy(self._create_compile_task())
                await self.compile_task
        except BuildError as e:
            raise BuildError(f"In module {self.name}:\n{e}")

    def __eq__(self, str):
        return self.name == str

    async def _create_new_task(self, name, from_modules=[]):
        # Info
        self.name        = name
        self.code_file   =            f"./module/{self.name.replace('.', '/').replace(':', '/')}.cpp"
        self.module_file = f"./bin/{type}/module/{self.name.replace('.', '.').replace(':', '-')}.{module_suffix}"
        self.object_file = f"./bin/{type}/module/{self.name.replace('.', '.').replace(':', '-')}.{object_suffix}"
        async with scheduler.schedule():
            self.content = await preprocess_file(code_file=self.code_file, name=self.name, module_file=self.module_file)

        # Check
        export_names = re.findall(r'^\s*export\s+module\s+([\w\.:]+)\s*;\s*$', self.content, flags=re.MULTILINE)
        if (len(export_names) != 1 or export_names[0] != self.name):
            raise BuildError(f"fatal error: file {self.code_file} should export module {self.name}")

        # Import
        self.from_modules = from_modules
        import_tasks = []
        import_names = re.findall(r'^\s*(?:export\s+)?import\s+([\w\.:]+)\s*;\s*$', self.content, flags=re.MULTILINE)
        for import_name in import_names:
            if import_name.startswith(':'):
                import_name = f"{self.name.partition(':')[0]}{import_name}"
            if import_name in self.from_modules:
                raise BuildError(f"fatal error: module dependency circle {' -> '.join(module.name for module in self.from_modules + [self] + [await Module(import_name)])}")
            import_tasks += [Module(import_name, from_modules=self.from_modules + [self])]
        self.import_modules = await asyncio.gather(*import_tasks)

        # Subtask
        if await Package.exist(self.name):
            await Package(self.name)

        # Status
        self.is_compiled = all(module.is_compiled for module in self.import_modules)                    and \
                           (not await Package.exist(self.name) or (await Package(self.name)).is_cached) and \
                           os.path.isfile(self.code_file)                                               and \
                           os.path.isfile(self.module_file)                                             and \
                           os.path.isfile(self.object_file)                                             and \
                           os.path.getmtime(self.code_file) <= os.path.getmtime(self.module_file)       and \
                           os.path.getmtime(self.code_file) <= os.path.getmtime(self.object_file)
        if not self.is_compiled:
            self.compile_task = None
            Module.total += 1
            
        # Return
        return self

    async def _create_compile_task(self):
        print(f"{self.name}._create_compile_task()")
        # Import && Subtask
        depend_tasks = []
        for import_module in self.import_modules:
            depend_tasks += [import_module.compile()]
        if await Package.exist(self.name) and not (await Package(self.name)).is_built:
            depend_tasks += [(await Package(self.name)).build()]
        await asyncio.gather(*depend_tasks)

        # Self
        async with scheduler.schedule():
            Module.current += 1
            print(f"compile module [{Module.current}/{Module.total}]: {self.name}")
            await compile_module(code_file   =self.code_file, 
                                 include_dirs=await recursive_find(node=self, func=Module._module_to_include_dir, root=True), 
                                 module_file =self.module_file, 
                                 object_file =self.object_file)
        
        # Status
        self.is_compiled = True

    async def _module_to_include_dir(module):
        return (await Package(module.name)).include_dir if await Package.exist(module.name) else None
