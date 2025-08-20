from common.algorithm  import recursive_find
from common.compiler   import link_object
from common.config     import argv, object_suffix, executable_suffix, static_suffix, shared_suffix
from common.error      import LogicError
from common.filesystem import exist_file, getmtime_file
from file.package      import Package
from file.source       import Source
import asyncio

class Object:
    pool    = {}
    current = 0
    total   = 0
    
    async def __new__(self, name):
        if name in Object.pool.keys():
            self = Object.pool[name]
        else:
            self = super().__new__(self)
            Object.pool[name] = self
            self.new_task = asyncio.create_task(self._create_new_task(name=name))
        await self.new_task
        return self
    
    async def link(self):
        if not self.is_linked:
            if self.link_task is None:
                self.link_task = asyncio.create_task(self._create_link_task())
            await self.link_task

    async def _create_new_task(self, name):
        try:
            # Info
            self.name        = name
            self.object_file = f"./bin/{argv.type}/source/{self.name.replace('.', '.').replace(':', '-')}.{object_suffix}"
            self.output_file = f"./bin/{argv.type}/source/{self.name.replace('.', '.').replace(':', '-')}.{globals().get(f'{argv.output}_suffix')}" if globals().get(f'{argv.output}_suffix') != "" else \
                               f"./bin/{argv.type}/source/{self.name.replace('.', '.').replace(':', '-')}"
            
            # Import
            await Source(self.name)

            # Status
            self.is_linked = (await Source(self.name)).is_compiled                                          and \
                             await exist_file(self.object_file)                                             and \
                             await exist_file(self.output_file)                                             and \
                             await getmtime_file(self.object_file) <= await getmtime_file(self.output_file)
            if not self.is_linked:
                self.link_task = None
                Object.total += 1

        except LogicError as e:
            raise e.add_prefix(f"In object {self.name}:")

    async def _create_link_task(self):
        try:
            # Import
            await (await Source(self.name)).compile()

            # Self
            await link_object(object_files =await recursive_find(node=await Source(self.name), func=Object._source_or_module_to_object_file, root=True               ),
                              library_files=await recursive_find(node=await Source(self.name), func=Object._module_to_library_files,         root=False, flatten=True),
                              output_file  =self.output_file,
                              on_start     =Object._print_progress(name=self.name))
            
            # Status
            self.is_linked = True
        
        except LogicError as e:
            raise e.add_prefix(f"In object {self.name}:")
        
    async def _source_or_module_to_object_file(source_or_module):
        return source_or_module.object_file
    
    async def _module_to_library_files(module):
        return (await Package(module.name)).library_files if await Package.exist(module.name) else None
    
    async def _print_progress(name):
        Object.current += 1
        print(f"link object [{Object.current}/{Object.total}]: {name}")
        

