import cppmake

async def build():
    await cppmake.include(
        name="stdexec",
        dir="./package/stdexec/include"
    )
    await cppmake.format(
        name="stdexec"
    )