import cppmake

async def build():
    await cppmake.include(
        name="proxy",
        dir="./package/proxy/include"
    )