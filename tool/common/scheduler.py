from common.config import parallel
import asyncio

class Scheduler:
    def __init__(self, available):
        self.max       = available
        self.available = available
        self._waiters  = []

    def schedule(self, requires=1):
        return Scheduler._Context(self, min(requires, self.max))

    async def _acquire(self, requires):
        future = asyncio.get_event_loop().create_future()
        self._waiters.append((requires, future))
        self._refresh()
        await future

    def _release(self, requires):
        self.available += requires
        self._refresh()

    def _refresh(self):
        refreshed_waiters = []
        for requires, future in self._waiters:
            if self.available >= requires:
                self.available -= requires
                future.set_result(True)
            else:
                refreshed_waiters.append((requires, future))
        self._waiters = refreshed_waiters

    class _Context:
        def __init__(self, scheduler, requires):
            self._scheduler = scheduler
            self._requires  = requires

        async def __aenter__(self):
            return await self._scheduler._acquire(self._requires)
        
        async def __aexit__(self, *args):
            self._scheduler._release(self._requires)

scheduler = Scheduler(available=parallel)