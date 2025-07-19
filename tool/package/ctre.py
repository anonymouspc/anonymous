from common.make import include, module

async def build():
    await include(
        name="ctre",
        dir="./package/ctre/include"
    )
    await module(
        name="ctre",
        file="./package/ctre/ctre.cppm"
    )