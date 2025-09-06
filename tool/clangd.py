import cppmake
import asyncio

async def build():
    await cppmake.Source("main")
    await asyncio.gather(module.compile(module_only=True) for module in cppmake.Module.pool)

cppmake.main(build())