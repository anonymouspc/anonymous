from common.config import argv, static_suffix
from common.make   import cmake, include, lib

async def build():
    await cmake(
        name="elements",
        dir="./package/elements",
        args=[
            "-DELEMENTS_BUILD_EXAMPLES=false"
        ]
    )

    await include(
        name="elements",
        dir="./package/elements/lib/include"
    )

    await include(
        name="elements",
        dir=f"./bin/{argv.type}/package/elements/build/_deps/cycfi_infra-src/include"
    )

    await include(
        name="elements",
        dir=f"./bin/{argv.type}/package/elements/build/_deps/asio-src/asio/include"
    )

    await include(
        name="elements",
        dir=f"./bin/{argv.type}/package/cairo/install/include/cairo"
    )

    await lib(
        name="elements",
        file=f"./bin/{argv.type}/package/elements/build/lib/libelements.{static_suffix}"
    )

"""
>>> cat package/elements/CMakeLists.txt | grep option
option(ELEMENTS_BUILD_EXAMPLES "build Elements library examples" ON)
option(ELEMENTS_ENABLE_LTO "enable link time optimization for Elements targets" OFF)
option(ELEMENTS_HOST_ONLY_WIN7 "If host UI library is win32, reduce elements features to support Windows 7" OFF)
"""