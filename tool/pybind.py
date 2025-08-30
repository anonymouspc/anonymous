import cppmake

async def pybind():
    await (await cppmake.Source("main")).compile(target="shared")
    
cppmake.wait(pybind())