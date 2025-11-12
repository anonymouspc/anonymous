from cppmake.basic.config          import config
from cppmake.logger.build_progress import build_progress_logger
from cppmake.system.all            import system
from cppmake.target.source         import Source
from cppmake.utility.decorator     import once, trace, unique
from cppmake.utility.process       import async_run
from cppmake.utility.scheduler     import scheduler

@unique
class Executable:
    @once
    @trace
    async def new(self, name):
        self.name            = name
        self.executable_file = f"./binary/{config.type}/source/{self.name.replace('.', '/')}{system.executable_suffix}"

    @once
    @trace
    async def run(self):
        await (await Source(self.name)).compile()
        async with scheduler.schedule():
            build_progress_logger.log("run executable", self)
            await async_run(command=[self.executable_file])
