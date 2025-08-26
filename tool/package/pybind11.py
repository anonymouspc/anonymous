from common.make import include, format

async def build():
    await include(
        name="pybind11",
        dir="./package/pybind11/include"
    )
    await format(
        name="pybind11"
    )