from common.make import cmake

async def build():
    await cmake(
        name="jpeg",
        dir="./package/jpeg",
        args=[
            "-DENABLE_SHARED=false",
            "-DENABLE_STATIC=true",
            "-DWITH_TOOLS=false",
            "-DWITH_TESTS=false",
            "-DWITH_FUZZ=false",
        ]
    )

"""
>>> cat ./package/jpeg/CMakeLists.txt | grep option
# 3. optionally provide a way to skip the installation of libjpeg-turbo
# 4. optionally provide a way to postfix target names, to avoid namespace
option(ENABLE_SHARED "Build shared libraries" TRUE)
option(ENABLE_STATIC "Build static libraries" TRUE)
option(REQUIRE_SIMD
option(WITH_ARITH_DEC
option(WITH_ARITH_ENC
  option(WITH_JAVA
option(WITH_JPEG7
option(WITH_JPEG8
option(WITH_SIMD "Include SIMD extensions, if available for this platform"
option(WITH_TURBOJPEG
option(WITH_TOOLS
option(WITH_TESTS "Enable regression tests, and build associated test programs (WARNING: Disable this at your own risk. If a build is not validated with the regression tests, then it is the responsibility of the builder to ensure, via other means, that the build produces mathematically correct results.)"
option(WITH_FUZZ "Build fuzz targets" FALSE)
macro(report_option var desc)
report_option(ENABLE_SHARED "Shared libraries")
report_option(ENABLE_STATIC "Static libraries")
report_option(WITH_ARITH_DEC "Arithmetic decoding support")
report_option(WITH_ARITH_ENC "Arithmetic encoding support")
report_option(WITH_TURBOJPEG "TurboJPEG API library")
report_option(WITH_JAVA "TurboJPEG Java wrapper")
report_option(WITH_TOOLS "Command-line tools")
report_option(WITH_TESTS "Regression tests")
  option(WITH_CRT_DLL
option(FORCE_INLINE "Force function inlining" TRUE)
# depending on the compiler and compiler options.  We leave it to the user to
# depending on the compiler and compiler options.  We leave it to the user to
"""