from cppmake.execution.operation import sync_wait
import asyncio
import functools
import inspect
import threading

def member  (cls):  ...
def once    (func): ...
def syncable(func): ...
def trace   (func): ...
def unique  (cls):  ...



def member(cls):
    assert inspect.isclass(cls)
    def memberizer(func):
        if type(func) != _Syncable:
            assert hasattr(cls, func.__name__) or func.__name__.startswith("_")# private functions which starts with '_' are not required to be pre-declared in class.
            setattr(cls, func.__name__, func)
        else:
            memberizer(func.sync_func)
            memberizer(func.async_func)
    return memberizer

def once(func):
    assert inspect.iscoroutinefunction(func)
    @functools.wraps(func)
    async def once_func(self, *args, **kwargs):
        if not         hasattr(self, f"_once_{func.__name__}"):
                       setattr(self, f"_once_{func.__name__}", {})
        if args not in getattr(self, f"_once_{func.__name__}").keys():
                       getattr(self, f"_once_{func.__name__}")[f"{args}_{kwargs}"] = asyncio.create_task(func(self, *args, **kwargs))
        return await   getattr(self, f"_once_{func.__name__}")[f"{args}_{kwargs}"]
    return once_func

def syncable(func):
    assert inspect.iscoroutinefunction(func) 
    assert func.__name__.startswith("async_") or func.__name__ == "__ainit__" 
    @functools.wraps(func)
    def sync_func(*args, **kwargs):
        value = None
        error = None
        def target():
            nonlocal value
            nonlocal error
            # try:
            value = sync_wait(func(*args, **kwargs))
            # except Exception as suberror:
            #     error = suberror
            # except KeyboardInterrupt as suberror:
            #     error = suberror
        thread = threading.Thread(target=target)
        thread.start()
        thread.join()
        if error is None:
            return value
        else:
            raise error
    sync_func.__name__ = func.__name__.removeprefix("async_") if func.__name__ != "__ainit__" else "__init__"
    return _Syncable(sync_func, func)

def trace(func):
    assert inspect.isfunction(func)
    if not inspect.iscoroutinefunction(func):
        @functools.wraps(func)
        def trace_func(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except Exception as error:
                if hasattr(error, "add_prefix"):
                    raise error.add_prefix(f"In {self.name}")
                else:
                    raise error
        return trace_func
    else:
        @functools.wraps(func)
        async def async_trace_func(self, *args, **kwargs):
            try:
                return await func(self, *args, **kwargs)
            except Exception as error:
                if hasattr(error, "add_prefix"):
                    raise error.add_prefix(f"In {type(self).__qualname__.lower()} {self.name}")
                else:
                    raise error
        return async_trace_func

def unique(cls):
    assert inspect.isclass(cls)
    setattr(cls, "_pool", {})
    if hasattr(cls, "__init__"):
        def __new__(cls, *args):
            if args in cls._pool.keys():
                self = cls._pool[args]
            else:
                self = super(cls, cls).__new__(cls)
                cls._pool[args] = self
            return self
        setattr(cls, "__new__", __new__)
    if hasattr(cls, "__ainit__"):
        async def __anew__(*args):
            if args in cls._pool.keys():
                self = cls._pool[args]
                await  getattr(self, "_unique_ainit")
            else:
                self = cls.__new__(cls, *args)
                cls._pool[args] = self
                if not hasattr(self, "_unique_ainit"):
                       setattr(self ,"_unique_ainit", asyncio.create_task(self.__ainit__(*args)))
                await  getattr(self, "_unique_ainit")
            return self
        setattr(cls, "__anew__", __anew__)
    return cls

class _Syncable:
    def __init__(self, sync_func, async_func):
        setattr(__import__(sync_func.__module__), sync_func.__name__, sync_func)
        self.sync_func = sync_func
        self.async_func = async_func
    async def __call__(self, *args, **kwargs):
        return await self.async_func(*args, **kwargs)