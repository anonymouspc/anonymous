from cppmake.basic.config        import config
from cppmake.execution.run       import async_run
from cppmake.execution.scheduler import scheduler
from cppmake.system.all          import system
from cppmake.unit.source         import Source
from cppmake.utility.decorator   import member, once, syncable, trace, unique

@unique
class Executable:
    def           __init__ (self, name): ...
    async def     __ainit__(self, name): ...
    def             run    (self):       ...
    async def async_run    (self):       ...

@member(Executable)
@syncable
@trace
async def __ainit__(self, name):
    self.name            = name
    self.executable_file = f"binary/{config.type}/source/{self.name.replace('.', '/')}{system.executable_suffix}"

@member(Executable)
@syncable
@once
@trace
async def async_run(self):
    await (await Source.__anew__(self.name)).async_compile()
    async with scheduler.schedule():
        await async_run(command=[self.executable_file])

