from cppmake.common.config import argv, shared_suffix
from cppmake.common.error  import LogicError
from cppmake.file.object   import Object
import asyncio

class Shared:
    pool    = {}
    current = 0
    total   = 0
    
    async def __new__(self, name):
        if name in Shared.pool.keys():
            self = Shared.pool[name]
        else:
            self = super().__new__(self)
            Shared.pool[name] = self
            self.new_task = asyncio.create_task(self._create_new_task(name=name))
        await self.new_task
        return self
        
    async def run(self):
        if not self.is_runned:
            if self.run_task is None:
                self.run_task = asyncio.create_task(self._create_run_task())
            await self.run_task
    

    
    async def _create_new_task(self, name):
        try:
            # Info
            self.name        = name
            self.shared_file = f"./bin/{argv.type}/source/{self.name.replace('.', '.').replace(':', '/')}.{shared_suffix}"
            
            # Import
            await Object(self.name)

        except LogicError as e:
            raise e.add_prefix(f"In shared {self.name}:")