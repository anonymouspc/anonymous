from cppmake.error.logic         import LogicError
from cppmake.execution.operation import sync_wait
import asyncio
import functools
import inspect
import threading

def member  (cls):  ...
def namable (func): ...
def once    (func): ...
def syncable(func): ...
def trace   (func): ...
def unique  (cls):  ...



def member(cls):
    assert inspect.isclass(cls)
    def memberizer(func):
        if inspect.isclass(func) or inspect.isfunction(func):
            assert hasattr(cls, func.__name__) or func.__name__.startswith("_") # private functions which starts with '_' are not required to be pre-declared in class.
            setattr(cls, func.__name__, func)
        elif type(func) == _Syncable: # memberize each subfunction from syncable.
            memberizer(func.func)
            memberizer(func.sync_func)
        else:
            assert False
    return memberizer

def namable(func):
    assert inspect.isfunction(func)
    if not inspect.iscoroutinefunction(func):
        @functools.wraps(func)
        def namable_func(self, *args, **kwargs):
            assert len(args) + len(kwargs) == 1
            if len(args) == 1:
                return func(self, *args)
            else:
                if "name" in kwargs.keys():
                    return func(self, name=kwargs["name"])
                else:
                    assert hasattr(type(self), f"{next(iter(kwargs.keys()))}_to_name")
                    return func(self, name=getattr(self, f"{next(iter(kwargs.keys()))}_to_name")(next(iter(kwargs.values()))))
        return namable_func
    else:
        @functools.wraps(func)
        async def async_namable_func(self, *args, **kwargs):
            assert len(args) + len(kwargs) == 1
            if len(args) == 1:
                return await func(self, *args)
            else:
                if "name" in kwargs.keys():
                    return await func(self, name=kwargs["name"])
                else:
                    assert hasattr(type(self), f"{next(iter(kwargs.keys()))}_to_name")
                    return await func(self, name=getattr(self, f"{next(iter(kwargs.keys()))}_to_name")(next(iter(kwargs.values()))))
        return async_namable_func
                

def once(func):
    assert inspect.iscoroutinefunction(func)
    @functools.wraps(func)
    async def once_func(self, *args, **kwargs):
        if not       hasattr(self, f"_once_{func.__name__}"):
                     setattr(self, f"_once_{func.__name__}", asyncio.create_task(func(self, *args, **kwargs)))
        return await getattr(self, f"_once_{func.__name__}")
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
            try:
                value = sync_wait(func(*args, **kwargs))
            except Exception as e:
                error = e
        thread = threading.Thread(target=target)
        thread.start()
        thread.join()
        if error is None:
            return value
        else:
            raise error
    sync_func.__name__ = func.__name__.removeprefix("async_") if func.__name__ != "__ainit__" else "__init__"
    return _Syncable(func, sync_func)

def trace(func):
    assert inspect.isfunction(func)
    if not inspect.iscoroutinefunction(func):
        @functools.wraps(func)
        def trace_func(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except LogicError as e:
                raise e.add_prefix(f"In {self.name}")
        return trace_func
    else:
        @functools.wraps(func)
        async def async_trace_func(self, *args, **kwargs):
            try:
                return await func(self, *args, **kwargs)
            except LogicError as e:
                raise e.add_prefix(f"In {type(self).__qualname__.lower()} {self.name}")
        return async_trace_func

def unique(cls):
    assert inspect.isclass(cls)
    setattr(cls, "_pool", {})
    def __new__(cls, *args):
        if args in cls._pool.keys():
            return cls._pool[args]
        else:
            self = super(cls, cls).__new__(cls)
            cls._pool[args] = self
            return self
    setattr(cls, "__new__", __new__)
    if hasattr(cls, "__ainit__"):
        async def __anew__(*args):
            self = cls.__new__(cls, *args)
            if not hasattr(self, "_unique_ainit"):
                   setattr(self ,"_unique_ainit", asyncio.create_task(self.__ainit__(*args)))
            await self._unique_ainit
        setattr(cls, "__anew__", __anew__)
    return cls

class _Syncable:
    def __init__(self, func, sync_func):
        self.func = func
        self.sync_func = sync_func
        setattr(__import__(sync_func.__module__), sync_func.__name__, sync_func)
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)