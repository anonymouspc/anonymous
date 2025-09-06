import asyncio

async def recursive_find(node, navigates, target, root=True, flatten=False):
    return await _recursive_find_with_cache(node, navigates, target, root, flatten, set())

##### private #####

async def _recursive_find_with_cache(node, navigates, target, root, flatten, cache):
    if root:
        if hasattr(node, target):
            if not flatten:
                cache |= set({getattr(node, target)})
            else:
                assert type(getattr(node, target)) is list
                cache |= set(getattr(node, target))

    async def subnav(navigate):
        if hasattr(node, navigate):
            if type(getattr(node, navigate)) is not list:
                await _recursive_find_with_cache(getattr(node, navigate), navigates, target, True, flatten, cache)
            else:
                await asyncio.gather(*[_recursive_find_with_cache(subnode, navigates, target, True, flatten, cache) for subnode in getattr(node, navigate)])
    await asyncio.gather(*[subnav(navigate) for navigate in navigates])

    return list(cache)
            