from common.config import parallel
import asyncio

class Scheduler():
    def __init__(self, value=1):
        if value < 0:
            raise ValueError("Scheduler initial value must be >= 0")
        self._waiters = None
        self._value = value
        self._max = value

    def locked(self):
        return self._value == 0 or (
            any(not w.cancelled() for w in (self._waiters.keys() if self._waiters is not None else [])))

    async def acquire(self, weight=1):
        if not self.locked():
            self._value -= weight
            return True

        if self._waiters is None:
            self._waiters = {}
        fut = asyncio.get_event_loop().create_future()
        self._waiters[fut] = weight
        try:
            try:
                await fut
            finally:
                self._waiters.pop(fut)
        except asyncio.CancelledError:
            if fut.done() and not fut.cancelled():
                self._value += weight
            raise

        finally:
            while self._value > 0:
                if not self._wake_up_next():
                    break
        return True

    def release(self, weight=1):
        self._value += weight
        self._wake_up_next()

    def _wake_up_next(self):
        if not self._waiters:
            return False

        for fut in self._waiters.keys():
            if not fut.done():
                self._value -= self._waiters[fut]
                fut.set_result(True)
                return True
        return False
    
    class _Context:
        def __init__(self, scheduler, weight):
            self._scheduler = scheduler
            self._weight    = weight

        async def __aenter__(self):
            return await self._scheduler.acquire(self._weight)

        async def __aexit__(self, *args):
            self._scheduler.release(self._weight)

    def schedule(self, weight=1):
        return Scheduler._Context(self, weight)

scheduler = Scheduler(value=parallel)