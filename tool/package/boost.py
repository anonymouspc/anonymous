from common.make import include
import os

async def build():
    for lib in os.listdir( "./package/boost/libs"):
        if os.path.isdir (f"./package/boost/libs/{lib}/include"):
            await include(
                name="boost",
                dir=f"./package/boost/libs/{lib}/include"
            )
        if os.path.isdir (f"./package/boost/libs/{lib}/src"):
            await include(
                name="boost",
                dir=f"./package/boost/libs/{lib}/src",
                relpath=f"./boost/{lib}/src"
            )

    for lib in os.listdir( "./package/boost/libs/numeric"):
        if os.path.isdir (f"./package/boost/libs/numeric/{lib}/include"):
            await include(
                name="boost",
                dir=f"./package/boost/libs/numeric/{lib}/include"
            )
        if os.path.isdir (f"./package/boost/libs/numeric/{lib}/src"):
            await include(
                name="boost",
                dir=f"./package/boost/libs/numeric/{lib}/src",
                relpath=f"./boost/numeric/{lib}/src"
            )