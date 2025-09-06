from cppmake.basic.context     import get_context
from cppmake.error.logic       import LogicError
from cppmake.utility.scheduler import scheduler
import asyncio
import functools

def context(func):
    @functools.wraps(func)
    async def wrapper(self, *args, **kwargs):
        if not hasattr(self.__class__, "tasks"):
               setattr(self.__class__, "tasks", [])
        if get_context() == "real":
            await func(self, *args, **kwargs)
        elif get_context() == "imag":
            innerfunc = func
            while hasattr(innerfunc, "__wrapped__"):
                innerfunc = innerfunc.__wrapped__
            try:
                innerfunc.__globals__["scheduler"] = _SkipScheduler()
                await func(self, *args, **kwargs)
            except _Skipped:
                pass
            async def task(self, *args, **kwargs):
                innerfunc.__globals__["scheduler"] = scheduler
                await func(self, *args, **kwargs)
            if not hasattr(self, "imag_runned"):
                   setattr(self, "imag_runned", True)
                   self.__class__.tasks += [task(self, *args, **kwargs)]
    wrapper.__name__ = f"{func.__name__}_context"
    return once(wrapper)

def once(func):
    @functools.wraps(func)
    async def wrapper(self, *args, **kwargs):
        if not       hasattr(self, f"{func.__name__}_{get_context()}_task"):
                     setattr(self, f"{func.__name__}_{get_context()}_task", asyncio.create_task(func(self, *args, **kwargs)))
        return await getattr(self, f"{func.__name__}_{get_context()}_task")
    wrapper.__name__ = f"{func.__name__}_once"
    return wrapper

def trace(func):
    @functools.wraps(func)
    async def wrapper(self, *args, **kwargs):
        try:
            await func(self, *args, **kwargs)
        except LogicError as e:
            raise e.add_prefix(f"In {self.__class__.__name__.lower()} {self.name}")
    wrapper.__name__ = f"{func.__name__}_trace"
    return wrapper

def unique(cls):
    cls.pool = {}
    async def __new__(cls, name):
        if name in cls.pool.keys():
            self = cls.pool[name]
        else:
            self = super(cls, cls).__new__(cls)
            cls.pool[name] = self
        await self.new(name)
        return self
    cls.__new__ = __new__
    return cls

##### private #####

class _SkipScheduler:
    max = 0

    def schedule(self, *args, **kwargs):
        return _SkipScheduler._Context()
    
    class _Context:
        async def __aenter__(self):
            raise _Skipped()
        
        async def __aexit__(self, *args):
            return True
        
class _Skipped(Exception):
    pass
