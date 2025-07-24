from common.compiler import run_executable
from common.config   import argv, executable_suffix
from common.error    import LogicError
from file.object     import Object
import asyncio

class Executable:
    pool    = {}
    current = 0
    total   = 0
    
    async def __new__(self, name):
        if name in Executable.pool.keys():
            self = Executable.pool[name]
        else:
            self = super().__new__(self)
            Executable.pool[name] = self
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
            self.name            = name
            self.executable_file = f"./bin/{argv.type}/source/{self.name.replace('.', '.').replace(':', '/')}.{executable_suffix}" if executable_suffix != "" else \
                                   f"./bin/{argv.type}/source/{self.name.replace('.' ,'.').replace(':', '/')}"
            
            # Import
            await Object(self.name)

            # Status
            self.is_runned = False # always assumed to be false
            self.run_task = None
            Executable.total += 1

        except LogicError as e:
            raise e.add_prefix(f"In executable {self.name}:")

    async def _create_run_task(self):
        try:
            # Import
            await (await Object(self.name)).link()

            # Self
            await run_executable(executable_file=f"./{self.executable_file}",
                                 on_start       =Executable._print_progress(name=self.name))

            # Status
            self.is_runned = True

        except LogicError as e:
            raise e.add_prefix(f"In executable {self.name}:")

    async def _print_progress(name):
        Executable.current += 1
        print(f"run executable [{Executable.current}/{Executable.total}]: {name}")