import cppmake

async def build():
    await (await cppmake.Source("main")).compile()

cppmake.sync_wait(build())