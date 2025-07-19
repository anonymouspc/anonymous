from common.make import include, module

async def build():
    await include(
        name="proxy",
        dir="./package/proxy/include"
    )
    await module(
        name="proxy",
        file="./package/proxy/include/proxy/v4/proxy.ixx",
        replace={"proxy.v4": "proxy"}
    )