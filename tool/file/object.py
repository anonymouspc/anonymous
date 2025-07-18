from common.algorithm import recursive_find
from common.compiler  import link_object
from common.config    import type, output, object_suffix, executable_suffix, static_suffix, shared_suffix
from common.error     import BuildError
from common.lazy      import Lazy
from common.scheduler import scheduler
from file.package     import Package
from file.source      import Source
import os

class Object:
    pool    = {}
    current = 0
    total   = 0
    
    async def __new__(self, name):
        try:
            if name in Object.pool.keys():
                self = Object.pool[name]
            else:
                self = super().__new__(self)
                Object.pool[name] = self
                self.new_task = Lazy(self._create_new_task(name=name))
            return await self.new_task
        except BuildError as e:
            raise BuildError(f"In object {self.name}:\n{e}")
        
    async def link(self):
        try:
            if not self.is_linked:
                if self.link_task is None:
                    self.link_task = Lazy(self._create_link_task())
                await self.link_task
        except BuildError as e:
            raise BuildError(f"In object {self.name}:\n{e}")

    async def _create_new_task(self, name):
        # Info
        self.name        = name
        self.object_file = f"./bin/{type}/source/{self.name.replace('.', '.').replace(':', '-')}.{object_suffix}"
        self.output_file = f"./bin/{type}/source/{self.name.replace('.', '.').replace(':', '-')}.{globals().get(f'{output}_suffix')}" if globals().get(f'{output}_suffix') != "" else \
                           f"./bin/{type}/source/{self.name.replace('.', '.').replace(':', '-')}"
        
        # Subtask
        await Source(self.name)

        # Status
        self.is_linked = (await Source(self.name)).is_compiled                                   and \
                         os.path.isfile(self.object_file)                                        and \
                         os.path.isfile(self.output_file)                                        and \
                         os.path.getmtime(self.object_file) <= os.path.getmtime(self.output_file)
        if not self.is_linked:
            self.link_task = None
            Object.total += 1

        # Return
        return self

    async def _create_link_task(self):
        # Subtask
        await (await Source(self.name)).compile()

        # Self
        async with scheduler.schedule():
            Object.current += 1
            print(f"link object [{Object.current}/{Object.total}]: {self.name}")
            await link_object(object_files =await recursive_find(node=await Source(self.name), func=Object._source_or_module_to_object_file, root=True               ),
                              library_files=await recursive_find(node=await Source(self.name), func=Object._module_to_library_files,         root=False, flatten=True),
                              output_file  =self.output_file)
        
        # Status
        self.is_linked = True
        
    async def _source_or_module_to_object_file(source_or_module):
        return source_or_module.object_file
    
    async def _module_to_library_files(module):
        return (await Package(module.name)).library_files if await Package.exist(module.name) else None
        

