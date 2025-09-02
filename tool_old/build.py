import cppmake

async def build():
    await cppmake.Source("main").compile()
    
cppmake.wait(build())