from cppmake.basic.context              import get_context
from cppmake.error.logic                import LogicError
from cppmake.logger.module_dependencies import module_dependencies_logger
from cppmake.utility.algorithm          import recursive_search
from cppmake.utility.scheduler          import scheduler
import asyncio
import functools
import inspect

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
        if not hasattr(self, "depcycle_ok"):
               setattr(self, "depcycle_ok", True)
               async def navigate(name):
                   return await module_dependencies_logger.get(name=name, code_file=f"./module/{name.replace('.', '/').replace(':', '/')}.cpp")
               def on_cycle(history):
                   raise LogicError(f"module import cycle [{' -> '.join(history)}]")
               await recursive_search(name, navigate=navigate, on_cycle=on_cycle)
        await func(self, name)
    wrapper.__name__ = f"{func.__name__}_depcycle"
    return wrapper

def deppkg(func):
    @functools.wraps(func)
    async def wrapper(self, name):
        await func(self, name)
        if "self" in      inspect.stack()[2].frame.f_locals.keys():
            from_module = inspect.stack()[2].frame.f_locals["self"]
            self.import_packages += [package for package in await 
                  recursive_search(from_module, navigate=lambda module:  module.import_modules,   collect =lambda module:  module.import_package) if package not in self.import_packages and package is not self and package is not None]
            await recursive_search(self,        navigate=lambda package: package.import_packages, on_cycle=lambda history: self.import_packages.remove(history[1]))
    wrapper.__name__ = f"{func.__name__}_deprev"
    return wrapper

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

async def _dfs():
    pass