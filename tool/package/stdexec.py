from common.make import include

async def build():
    await include(
        name="stdexec",
        dir="./package/stdexec/include"
    )