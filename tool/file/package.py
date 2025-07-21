from common.config import type, static_suffix, shared_suffix
import asyncio
import importlib
import os

class Package:
    pool    = {}
    current = 0
    total   = 0

    async def __new__(self, name):
        name = name.partition('.')[0]
        if name in Package.pool.keys():
            self = Package.pool[name]
        else:
            self = super().__new__(self)
            Package.pool[name] = self
            self.new_task = asyncio.create_task(self._create_new_task(name=name))
        await self.new_task
        return self
    
    async def build(self):
        if not self.is_built:
            if self.build_task is None:
                self.build_task = asyncio.create_task(self._create_build_task())
            await self.build_task

    async def exist(name):
        name = name.partition('.')[0]
        return os.path.isfile(f"./tool/package/{name}.py")

    def __eq__(self, str):
        return self.name == str

    async def _create_new_task(self, name):
        # Info
        self.name          = name
        self.package_file  =  f"./tool/package/{self.name.replace('.', '/').replace(':', '/')}.py"
        self.build_dir     =  f"./bin/{type}/package/{self.name}/build"
        self.install_dir   =  f"./bin/{type}/package/{self.name}/install"
        self.include_dir   =  f"./bin/{type}/package/{self.name}/install/include"
        self.lib_dir       =  f"./bin/{type}/package/{self.name}/install/lib"
        self.library_files = [                           f"./bin/{type}/package/{self.name}/install/lib/{file}"                                                                                  \
                              for file in os.listdir    (f"./bin/{type}/package/{self.name}/install/lib")                                                                                        \
                              if          os.path.isfile(f"./bin/{type}/package/{self.name}/install/lib/{file}") and (file.endswith(f".{static_suffix}") or file.endswith(f".{shared_suffix}"))] \
                              if          os.path.isdir (f"./bin/{type}/package/{self.name}/install/lib") else []
        
        # Import
        self.import_packages = [] # Managed by Module
        
        # Status
        self.is_built    = False
        self.is_cached   = os.path.isdir(self.install_dir) # Some header-only packages only generate install_dir but not build_dir
        self.tool_module = importlib.import_module(f"package.{self.name}")
        self.build_task  = None
        if not self.is_cached:
            Package.total += 1

        # Self
        if hasattr(self.tool_module, "initialize"):
            await self.tool_module.initialize()

        # Check
        assert await Package.exist(self.name)
        
    async def _create_build_task(self):
        # Import
        await asyncio.gather(*[package.build() for package in self.import_packages])

        # Self
        if hasattr(self.tool_module, "build"):
            await self.tool_module.build()
            self.library_files = [                           f"./bin/{type}/package/{self.name}/install/lib/{file}"                                                                                  \
                                  for file in os.listdir    (f"./bin/{type}/package/{self.name}/install/lib")                                                                                        \
                                  if          os.path.isfile(f"./bin/{type}/package/{self.name}/install/lib/{file}") and (file.endswith(f".{static_suffix}") or file.endswith(f".{shared_suffix}"))] \
                                  if          os.path.isdir (f"./bin/{type}/package/{self.name}/install/lib") else []

        # Status
        self.is_built = True

    async def _module_to_package(module):
        return await Package(module.name) if await Package.exist(module.name) else None