import cppmake

async def build():
    await cppmake.include(
        name="pybind11",
        dir="./package/pybind11/include"
    )
    await cppmake.format(
        name="pybind11"
    )