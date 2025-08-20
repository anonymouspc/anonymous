from common.make  import include, format

async def build():
    await include(
        name="eigen",
        dir="./package/eigen/Eigen",
        relpath="Eigen"
    )
    await include(
        name="eigen",
        dir="./package/eigen/unsupported/Eigen",
        relpath="unsupported/Eigen"
    )
    await format(
        name="eigen"
    )
