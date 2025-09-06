import cppmake

async def build():
    await (await cppmake.Source("main")).compile()

cppmake.main(build())