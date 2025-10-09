import cppmake

async def build():
    await cppmake.include(
        name="eigen",
        dir="./package/eigen/Eigen",
        relpath="Eigen"
    )
    await cppmake.include(
        name="eigen",
        dir="./package/eigen/unsupported/Eigen",
        relpath="unsupported/Eigen"
    )
    await cppmake.format(
        name="eigen"
    )
