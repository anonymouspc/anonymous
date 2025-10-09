import cppmake

async def build():
    await cppmake.include(
        name="ctre",
        dir="./package/ctre/include"
    )