from common.make import cmake

async def build():
    await cmake(
        name="zlib",
        dir="./package/zlib",
        args=[
            "-DZLIB_BUILD_TESTING=false",
            "-DZLIB_BUILD_SHARED=false",
            "-DZLIB_BUILD_STATIC=true",
            "-DZLIB_BUILD_MINIZIP=false"
        ]
    )

"""
>>> cat ./package/zlib/CMakeLists.txt | grep option
option(ZLIB_BUILD_TESTING "Enable Zlib Examples as tests" ON)
option(ZLIB_BUILD_SHARED "Enable building zlib shared library" ON)
option(ZLIB_BUILD_STATIC "Enable building zlib static library" ON)
option(ZLIB_BUILD_MINIZIP "Enable building libminizip contrib library" OFF)
option(ZLIB_INSTALL "Enable installation of zlib" ON)
option(ZLIB_PREFIX "prefix for all types and library functions, see zconf.h.in"
    option(ZLIB_INSTALL_COMPAT_DLL "Install a copy as zlib1.dll" ON)
"""