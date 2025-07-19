from common.make import include

async def build():
    await include(
        name="pybind11",
        dir="./package/pybind11/include"
    )