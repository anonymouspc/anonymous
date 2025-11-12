import asyncio
import inspect

def member(cls):
    def decorator(func):
        assert hasattr(cls, func.__name__)
        setattr(cls, func.__name__, func)
        syncable(cls)
        return func
    return decorator

def syncable(cls):
    for name, member in inspect.getmembers(cls):
        if name.startswith("async_") and inspect.iscoroutinefunction(member):
            def decorator(self, *args, func=member, **kwargs):
                asyncio.run(func(self, *args, **kwargs)) # sync_wait
            setattr(cls, name.removeprefix("async_"), decorator)
    return cls

@syncable
class Clang:
    async def async_hello(self): ...


@member(Clang)
async def async_hello(self):
    print("world")


Clang().hello()