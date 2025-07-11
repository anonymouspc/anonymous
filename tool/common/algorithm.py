def recursive_find(node, func, root=True, flatten=False):
    return _recursive_find_with_cache(node=node, func=func, root=root, flatten=flatten, cache=[])

def _recursive_find_with_cache(node, func, root, flatten, cache):
    if root:
        result = func(node)
        if result is not None:
            if not flatten:
                if result not in cache:
                    cache += [result]
            else:
                for element in result:
                    if element not in cache:
                        cache += [element]

    for import_module in node.import_modules:
        _recursive_find_with_cache(node=import_module, func=func, root=True, flatten=flatten, cache=cache)

    return cache