import cppmake

async def build():
    await cppmake.Source("main").compile()

cppmake.main(build())