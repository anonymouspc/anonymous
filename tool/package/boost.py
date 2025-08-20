from common.filesystem import exist_dir, iterate_dir, base_path
from common.make       import include, format

async def build():
    async for library_dir in iterate_dir("./package/boost/libs"):
        if await exist_dir(f"{library_dir}/include"):
            await include(
                name="boost",
                dir=f"{library_dir}/include"
            )
        if await exist_dir(f"{library_dir}/src"):
            await include(
                name="boost",
                dir=f"{library_dir}/src",
                relpath=f"boost/{base_path(library_dir)}/src"
            )

    async for library_dir in iterate_dir( "./package/boost/libs/numeric"):
        if await exist_dir(f"{library_dir}/include"):
            await include(
                name="boost",
                dir=f"{library_dir}/include"
            )
        if await exist_dir(f"{library_dir}/src"):
            await include(
                name="boost",
                dir=f"{library_dir}/src",
                relpath=f"boost/numeric/{base_path(library_dir)}/src"
            )
    await format(
        name="boost",
        relpath="boost/asio"
    )
    await format(
        name="boost",
        relpath="boost/fusion"
    )
    await format(
        name="boost",
        relpath="boost/mpl"
    )
    await format(
        name="boost",
        relpath="boost/system"
    )