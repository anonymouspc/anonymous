from cppmake.error.logic                import LogicError
from cppmake.logger.module_dependencies import module_dependencies_logger
from cppmake.utility.algorithm          import recursive_search
from cppmake.utility.filesystem         import iterate_dir
from cppmake.utility.scheduler          import scheduler
import asyncio
import functools

def context(func):
    context._value = "real"
    def get():
        return context._value
    context.get = get
    def set(new_value):
        context._value = new_value
    context.set = set
    @functools.wraps(func)
    async def wrapper(self, *args, **kwargs):
        if not hasattr(self.__class__, "tasks"):
               setattr(self.__class__, "tasks", [])
        if context.get() == "real":
            await func(self, *args, **kwargs)
        elif context.get() == "imag":
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
            if (hasattr(self, "is_built"   ) and not self.is_built   ()) or \
               (hasattr(self, "is_compiled") and not self.is_compiled()):
                if not hasattr(self, "imag_runned"):
                       setattr(self, "imag_runned", True)
                       self.__class__.tasks += [task(self, *args, **kwargs)]
    wrapper.__name__ = f"{func.__name__}_context"
    return wrapper

def depmod(func):
    @functools.wraps(func)
    async def wrapper(self, name):
        if not hasattr(self, "depmod_ok"):
               setattr(self, "depmod_ok", True)
               async def navigate(name):
                   return await module_dependencies_logger.get(name=name, code_file=f"./module/{name.replace('.', '/').replace(':', '/')}.cpp")
               def on_cycle(history):
                   raise LogicError(f"module import cycle [{' -> '.join(history)}]")
               await recursive_search(name, navigate=navigate, on_cycle=on_cycle)
        await func(self, name)
    wrapper.__name__ = f"{func.__name__}_depmod"
    return wrapper

def deppkg(func):
    @functools.wraps(func)
    async def wrapper(self, name):
        if not hasattr(self, "deppkg_ok"):
               setattr(self, "deppkg_ok", True)
               async def navigate(name):
                   return await ...
               def on_cycle(history):
                   raise LogicError(f"package import cycle [{' -> '.join(history)}]")
               await recursive_search(name, navigate=navigate, on_cycle=on_cycle)
               await func(self, name)
    wrapper.__name__ = f"{func.__name__}_deppkg"
    return wrapper

def once(func):
    @functools.wraps(func)
    async def wrapper(self, *args, **kwargs):
        if not       hasattr(self, f"{func.__name__}_{context.get()}_task"):
                     setattr(self, f"{func.__name__}_{context.get()}_task", asyncio.create_task(func(self, *args, **kwargs)))
        return await getattr(self, f"{func.__name__}_{context.get()}_task")
    wrapper.__name__ = f"{func.__name__}_once"
    return wrapper

def storetrue(func):
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, f"{func.__name__}_cache"):
               setattr(self, f"{func.__name__}_cache", False)
        if     getattr(self, f"{func.__name__}_cache") == True:
            return True
        else:
            result = func(self, *args, **kwargs)
            if result == True:
               setattr(self, f"{func.__name__}_cache", True)
            return result
    wrapper.__name__ = f"{func.__name__}_storetrue"
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
    def __eq__(self1, self2):
        return self1 is self2
    cls.__new__ = __new__
    cls.__eq__  = __eq__
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

async def _throw(exception):
    raise exception