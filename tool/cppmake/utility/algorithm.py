from cppmake.execution.operation import when_all

def             recursive_collect(*args, **kwargs): ...
async def async_recursive_collect(*args, **kwargs): ...



def recursive_collect(root, next, collect, on_root):
    return _recursive_collect_impl(root, next, collect, on_root, cached=list(), visited=set())

def _recursive_collect_impl(node, next, collect, on_root, cached, visited):
    if node not in visited:
        visited |= {node}
        if on_root:
            try:
                cached += [collect(node)]
            except AttributeError:
                pass
        for subnode in next(node):
            _recursive_collect_impl(subnode, next, collect, True, cached, visited)
    return cached

async def async_recursive_collect(root, next, collect, on_root):
    return await _async_recursive_collect_impl(root, next, collect, on_root, cached=list(), visited=set())

async def _async_recursive_collect_impl(node, next, collect, on_root, cached, visited):
    if node not in visited:
        visited |= {node}
        if on_root:
            try:
                cached += [collect(node)]
            except AttributeError:
                pass
        await when_all([_async_recursive_collect_impl(subnode, next, collect, True, cached, visited) for subnode in await next(node)])
    return cached
