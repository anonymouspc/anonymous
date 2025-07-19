from common.algorithm import recursive_find
from common.config    import type, static_suffix, shared_suffix
from common.error     import BuildError
from common.lazy      import Lazy
from common.scheduler import scheduler
import asyncio
import importlib
import os

class Package:
    pool    = {}
    current = 0
    total   = 0

    async def __new__(self, name, by_module=None):
        try:
            name = name.partition('.')[0]
            if name in Package.pool.keys():
                Package.pool[name].by_modules += [by_module] if by_module is not None else []
                self = Package.pool[name]
            else:
                self = super().__new__(self)
                self.by_modules = [by_module] if by_module is not None else []
                Package.pool[name] = self
                self.new_task = Lazy(self._create_new_task(name=name))
            return await self.new_task
        except BuildError as e:
            raise BuildError(f"In package {self.name}:\n{e}")
    
    async def build(self, _from_packages=[]):
        try:
            if not self.is_built:
                if self.build_task is None:
                    self.build_task = Lazy(self._create_build_task(_from_packages=_from_packages))
                await self.build_task
        except BuildError as e:
            raise BuildError(f"In package {self.name}:\n{e}")
        except Exception as e:
            print(f"package {self.name} build error")
            raise e

    async def exist(name):
        name = name.partition('.')[0]
        return os.path.isfile(f"./tool/package/{name}.py")

    def __eq__(self, str):
        return self.name == str

    async def _create_new_task(self, name):
        # Info
        self.name          = name
        self.package_file  =  f"./tool/package/{self.name.replace('.', '/').replace(':', '/')}.py"
        self.install_dir   =  f"./bin/{type}/package/{self.name}/install"
        self.include_dir   =  f"./bin/{type}/package/{self.name}/install/include"
        self.library_files = [f"./bin/{type}/package/{self.name}/install/lib/{file}"                                                                                                              \
                              for file in os.listdir    (f"./bin/{type}/package/{self.name}/install/lib")                                                                                         \
                              if          os.path.isfile(f"./bin/{type}/package/{self.name}/install/lib/{file}") and (file.endswith(f".{static_suffix}") or file.endswith(f".{shared_suffix}"))] \
                              if          os.path.isdir (f"./bin/{type}/package/{self.name}/install/lib") else []
        
        # Status
        self.is_built    = False
        self.is_cached   = os.path.isdir(self.install_dir)
        self.tool_module = importlib.import_module(f"package.{self.name}")
        if hasattr(self.tool_module, "initialize"):
            await self.tool_module.initialize()
        self.build_task = None
        if not self.is_cached:
            Package.total += 1

        # Check
        assert await Package.exist(self.name)

        # Return
        return self
    
    async def _create_build_task(self, _from_packages=[]):
        # Import
        depend_tasks = []
        for by_module in self.by_modules:
            for import_package in await recursive_find(node=by_module, func=Package._module_to_package):
                if import_package not in _from_packages and import_package is not self:
                    depend_tasks += [import_package.build(_from_packages=_from_packages + [self])]
        await asyncio.gather(*depend_tasks)

        # Self
        if hasattr(self.tool_module, "build"):
            if self.is_cached:
                async with scheduler.schedule():
                    await self.tool_module.build()
            else:
                async with scheduler.schedule(os.cpu_count()):
                    Package.current += 1
                    print(f"build package [{Package.current}/{Package.total}]: {self.name}")
                    await self.tool_module.build()

            self.library_files = [f"./bin/{type}/package/{self.name}/install/lib/{file}"                                                                                                              \
                                  for file in os.listdir    (f"./bin/{type}/package/{self.name}/install/lib")                                                                                         \
                                  if          os.path.isfile(f"./bin/{type}/package/{self.name}/install/lib/{file}") and (file.endswith(f".{static_suffix}") or file.endswith(f".{shared_suffix}"))] \
                                  if          os.path.isdir (f"./bin/{type}/package/{self.name}/install/lib") else []

        # Status
        self.is_built = True

    async def _module_to_package(module):
        return await Package(module.name) if await Package.exist(module.name) else None