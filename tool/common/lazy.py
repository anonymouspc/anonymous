import asyncio

class Lazy:
    def __init__(self, coro):
        self._coro = coro
        self._task = None

    def __await__(self):
        if self._task is None:
            self._task = asyncio.create_task(self._coro)
        return self._task.__await__()