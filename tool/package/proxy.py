import cppmake

async def build():
    await cppmake.include(
        name="proxy",
        dir="./package/proxy/include"
    )
    await cppmake.module(
        name="proxy",
        file="./package/proxy/include/proxy/v4/proxy.ixx",
    )