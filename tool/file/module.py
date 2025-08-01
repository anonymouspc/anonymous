from common.algorithm import recursive_find
from common.config    import argv, module_suffix, object_suffix
from common.compiler  import preprocess_file, compile_module
from common.error     import LogicError
from file.package     import Package
import asyncio
import os
import re

class Module:
    pool    = {}
    current = 0
    total   = 0
    topo    = {}

    async def __new__(self, name, recurse_submodules=True):
        if name in Module.pool.keys():
            self = Module.pool[name]
        else:
            self = super().__new__(self)
            Module.pool[name] = self
            Module.topo[name] = len(Module.topo)
            self.new_task_stage_1 = asyncio.create_task(self._create_new_task_stage_1(name=name))
            self.new_task_stage_2 = None
        await self.new_task_stage_1
        if recurse_submodules:
            if self.new_task_stage_2 is None:
                self.new_task_stage_2 = asyncio.create_task(self._create_new_task_stage_2(name=name))
            await self.new_task_stage_2
        return self

    async def compile(self):
        if not self.is_compiled:
            if self.compile_task is None:
                self.compile_task = asyncio.create_task(self._create_compile_task())
            await self.compile_task

    def __eq__(self, str):
        return self.name == str

    async def _create_new_task_stage_1(self, name):
        try:
            # Info
            self.name        = name
            self.code_file   =                 f"./module/{self.name.replace('.', '/').replace(':', '/')}.cpp"
            self.module_file = f"./bin/{argv.type}/module/{self.name.replace('.', '.').replace(':', '-')}.{module_suffix}"
            self.object_file = f"./bin/{argv.type}/module/{self.name.replace('.', '.').replace(':', '-')}.{object_suffix}"
            self.content     = await preprocess_file(code_file=self.code_file, name=self.name, module_file=self.module_file)

            # Check
            export_names = re.findall(r'^\s*export\s+module\s+([\w\.:]+)\s*;\s*$', self.content, flags=re.MULTILINE)
            if (len(export_names) != 1 or export_names[0] != self.name):
                raise LogicError(f"file {self.code_file} export module {export_names} but expect to export module {[self.name]}")

            # Import
            self.import_names = [import_name if not import_name.startswith(':') else f"{self.name.partition(':')[0]}{import_name}" 
                                 for import_name in re.findall(r'^\s*(?:export\s+)?import\s+([\w\.:]+)\s*;\s*$', self.content, flags=re.MULTILINE)]
        
        except LogicError as e:
            raise e.add_prefix(f"In module {self.name}:")

    async def _create_new_task_stage_2(self, name):
        try:
            await self.new_task_stage_1

            # Check
            await asyncio.gather(*[Module._check_dependency_cycle(from_name=self.name, to_name=import_name) for import_name in self.import_names])

            # Import
            self.import_modules = await asyncio.gather(*[Module(import_name) for import_name in self.import_names])
            if await Package.exist(self.name):
                await Package(self.name)
                (await Package(self.name)).import_packages += [await Package(import_module.name) for import_module in self.import_modules if await Package.exist(import_module.name) and await Package(self.name) is not await Package(import_module.name)]

            # Status
            self.is_compiled = all(module.is_compiled for module in self.import_modules)                   and \
                               (not await Package.exist(self.name) or (await Package(self.name)).is_built) and \
                               os.path.isfile(self.code_file)                                              and \
                               os.path.isfile(self.module_file)                                            and \
                               os.path.isfile(self.object_file)                                            and \
                               os.path.getmtime(self.code_file) <= os.path.getmtime(self.module_file)      and \
                               os.path.getmtime(self.code_file) <= os.path.getmtime(self.object_file)
            if not self.is_compiled:
                self.compile_task = None
                Module.total += 1
            
        except LogicError as e:
            raise e.add_prefix(f"In module {self.name}:")

    async def _create_compile_task(self):
        # Import
        depend_tasks = []
        for import_module in self.import_modules:
            depend_tasks += [import_module.compile()]
        if await Package.exist(self.name) and not (await Package(self.name)).is_built:
            depend_tasks += [(await Package(self.name)).build()]
        await asyncio.gather(*depend_tasks)

        # Self
        await compile_module(code_file   =self.code_file, 
                             include_dirs=await recursive_find(node=self, func=Module._module_to_include_dir, root=True), 
                             module_file =self.module_file, 
                             object_file =self.object_file,
                             on_start    =Module._print_progress(name=self.name))
    
        # Status
        self.is_compiled = True

    async def _check_dependency_cycle(from_name, to_name):
        await Module(to_name, recurse_submodules=False)
        if Module.topo[from_name] < Module.topo[to_name]:
            pass
        else:
            history_names = [from_name]
            visited_names = set()
            await Module._check_dependency_cycle_dfs(from_name=from_name, current_name=to_name, history_names=history_names, visited_names=visited_names)

    async def _check_dependency_cycle_dfs(from_name, current_name, history_names, visited_names):
        current_module = await Module(current_name, recurse_submodules=False)
        if current_name == from_name:
            raise LogicError(f"dependency cycle {' -> '.join(history_names + [current_name])}")
        if current_name in visited_names:
            return
        visited_names.add(current_name)
        await asyncio.gather(*[Module._check_dependency_cycle_dfs(from_name=from_name, current_name=import_name, history_names=history_names + [current_name], visited_names=visited_names) for import_name in current_module.import_names])
    
    async def _module_to_include_dir(module):
        return (await Package(module.name)).include_dir if await Package.exist(module.name) else None
    
    async def _print_progress(name):
        Module.current += 1
        print(f"compile module [{Module.current}/{Module.total}]: {name}")