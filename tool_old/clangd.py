import cppmake

async def clangd():
    await cppmake.Source("main")
    await asyncio.gather)