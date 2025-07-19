from common.compiler  import run_executable
from common.config    import executable_suffix, type
from common.error     import BuildError
from common.lazy      import Lazy
from common.scheduler import scheduler
from file.object      import Object
import asyncio

class Executable:
    pool    = {}
    current = 0
    total   = 0
    
    async def __new__(self, name):
        try:
            if name in Executable.pool.keys():
                self = Executable.pool[name]
            else:
                self = super().__new__(self)
                Executable.pool[name] = self
                self.new_task = Lazy(self._create_new_task(name=name))
            return await self.new_task
        except BuildError as e:
            raise BuildError(f"In executable {self.name}:\n{e}")
        
    async def run(self):
        try:
            if not self.is_runned:
                if self.run_task is None:
                    self.run_task = Lazy(self._create_run_task())
                await self.run_task
        except BuildError as e:
            raise BuildError(f"In executable {self.name}:\n{e}")
    
    async def _create_new_task(self, name):
        # Info
        self.name            = name
        self.executable_file = f"./bin/{type}/source/{self.name.replace('.', '.').replace(':', '/')}.{executable_suffix}" if executable_suffix != "" else \
                               f"./bin/{type}/source/{self.name.replace('.' ,'.').replace(':', '/')}"
        
        # Subtask
        await Object(self.name)

        # Status
        self.is_runned = False # always assumed to be false
        self.run_task = None
        Executable.total += 1

        # Return
        return self

    async def _create_run_task(self):
        # Subtask
        await (await Object(self.name)).link()

        # Self
        async with scheduler.schedule():
            Executable.current += 1
            print(f"run executable [{Executable.current}/{Executable.total}]: {self.name}")
            await run_executable(executable_file=f"./{self.executable_file}")

        # Status
        self.is_runned = True