import cppmake

async def build():
    await cppmake.include(
        name="ctre",
        dir="./package/ctre/include"
    )
    await cppmake.module(
        name="ctre",
        file="./package/ctre/ctre.cppm"
    )