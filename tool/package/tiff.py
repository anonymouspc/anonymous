from common.make import cmake

async def build():
    await cmake(
        name="tiff",
        dir="./package/tiff",
        args=[
            "-DBUILD_SHARED_LIBS=false",
            "-Dtiff-static=true",
            "-Dtiff-tools=false",
            "-Dtiff-tests=false",
            "-Dtiff-contrib=false",
            "-Dtiff-docs=false",
        ]
    )

"""
>>> cat ./package/tiff/CMakeLists.txt | grep option
  option(BUILD_SHARED_LIBS "Build shared libraries" ON)
option(tiff-static "build TIFF static libraries" ${TIFF_STATIC_LIBS_DEFAULT})
option(tiff-tools "build TIFF tools" ON)
option(tiff-tests "build TIFF tests" ON)
option(tiff-contrib "build TIFF contrib" ON)
option(tiff-docs "build TIFF documentation" ON)
option(tiff-deprecated "build TIFF deprecated features" OFF)
option(tiff-install "install TIFF targets" ${TIFF_INSTALL_DEFAULT})
"""