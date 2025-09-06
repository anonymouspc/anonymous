import cppmake

async def build():
    for library_dir in cppmake.iterate_dir("./package/boost/libs"):
        if cppmake.exist_dir(f"{library_dir}/include"):
            await cppmake.include(
                name="boost",
                dir=f"{library_dir}/include"
            )
        if cppmake.exist_dir(f"{library_dir}/src"):
            await cppmake.include(
                name="boost",
                dir=f"{library_dir}/src",
                relpath=f"boost/{cppmake.base_path(library_dir)}/src"
            )

    for library_dir in cppmake.iterate_dir( "./package/boost/libs/numeric"):
        if cppmake.exist_dir(f"{library_dir}/include"):
            await cppmake.include(
                name="boost",
                dir=f"{library_dir}/include"
            )
        if cppmake.exist_dir(f"{library_dir}/src"):
            await cppmake.include(
                name="boost",
                dir=f"{library_dir}/src",
                relpath=f"boost/numeric/{cppmake.base_path(library_dir)}/src"
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