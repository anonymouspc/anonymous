from common.make import include, format

async def build():
    await include(
        name="stdexec",
        dir="./package/stdexec/include"
    )
    await format(
        name="stdexec"
    )