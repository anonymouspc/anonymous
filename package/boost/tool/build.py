import cppmake

async def build():
    await cppmake.cmake(
        name="boost",
        dir="./package/boost",
        args=[
            "-DBUILD_SHARED_LIBS=false",
           f"-DBOOST_INCLUDE_LIBRARIES={';'.join([file.removeprefix("./module/boost/").removesuffix(".cpp") for file in cppmake.iterate_dir("./module/boost", file_only=True)])}"
        ]
    )
    await cppmake.format(
        name="boost",
        relpath="boost/asio"
    )
    await cppmake.format(
        name="boost",
        relpath="boost/fusion"
    )
    await cppmake.format(
        name="boost",
        relpath="boost/mpl"
    )
    await cppmake.format(
        name="boost",
        relpath="boost/system"
    )