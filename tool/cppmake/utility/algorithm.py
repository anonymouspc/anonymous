import asyncio

async def recursive_search(node, navigate, collect=None, root=True, flatten=False, on_cycle=None):
    return await _recursive_search_with_cache(node, navigate, collect, root, flatten, on_cycle, list(), set(), list())

##### private #####

async def _recursive_search_with_cache(node, navigate, collect, root, flatten, on_cycle, cache, visited, history):
    if on_cycle is not None:
        if len(history) >= 1 and node == history[0]:
            on_cycle(history + [node])
    if node in visited:
        return cache
    else:
        visited |= {node}
        if root and collect is not None:
            try:
                new_cache = collect(node)
                if not flatten:
                    cache += [new_cache] if new_cache is not None else []
                else:
                    assert type(new_cache) is list
                    cache += [item for item in new_cache if item is not None]
            except AttributeError:
                pass
        if not asyncio.iscoroutinefunction(navigate):
            await asyncio.gather(*[_recursive_search_with_cache(subnode, navigate, collect, True, flatten, on_cycle, cache, visited, history + [node]) for subnode in       navigate(node) if subnode is not None])
        else:
            await asyncio.gather(*[_recursive_search_with_cache(subnode, navigate, collect, True, flatten, on_cycle, cache, visited, history + [node]) for subnode in await navigate(node) if subnode is not None])
        return list(set(cache))