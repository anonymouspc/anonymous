import asyncio
from collections import defaultdict

class DependencyCycleError(Exception):
    pass

header_cache = {}
in_progress = set()
dependencies = defaultdict(set)

async def build_header(name: str):
    # 如果当前节点已经在构建中 → 有循环依赖
    if name in in_progress:
        # 构造环路信息
        cycle = find_cycle(name)
        raise DependencyCycleError(f"Dependency cycle detected: {cycle}")

    in_progress.add(name)

    print(f"Building {name} ...")

    deps = header_dependencies[name]

    for dep in deps:
        dependencies[name].add(dep)
        await Header.async_create(dep)

    in_progress.remove(name)

    return f"Header({name}) built"


def find_cycle(start):
    """从依赖图中找出一个环路，用于报错"""
    visited = set()
    stack = []

    def dfs(node):
        if node in stack:
            idx = stack.index(node)
            return stack[idx:] + [node]  # cycle slice

        if node in visited:
            return None
        visited.add(node)

        stack.append(node)
        for nxt in dependencies[node]:
            cycle = dfs(nxt)
            if cycle:
                return cycle
        stack.pop()

    return " -> ".join(dfs(start))


class Header:
    @staticmethod
    async def async_create(name: str):
        # 异步唯一
        if name not in header_cache:
            header_cache[name] = asyncio.create_task(build_header(name))

        return await header_cache[name]


# ---- 示例依赖 ----
header_dependencies = {
    "A": ["B"],
    "B": ["A"],    # 循环！
    "X": ["A", "B"]
}
# ------------------

async def main():
    try:
        await Header.async_create("X")
    except DependencyCycleError as e:
        print("\nERROR:", e)

asyncio.run(main())
