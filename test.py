import asyncio
import random

class Package:
    async def build(self):
        print("build package")
        return await asyncio.sleep(random.randint(3, 5))

class Module:
    async def compile(self):
        print("compile module")
        return await asyncio.sleep(random.randint(1, 3))

packages = [Package(), Package(), Package()]
modules  = [Module(),  Module(),  Module() ]


async def main():
    await asyncio.gather(*(package.build() for package in packages))
    await asyncio.gather(*(module.compile() for module in modules))

asyncio.run(main())