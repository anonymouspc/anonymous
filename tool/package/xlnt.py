import cppmake

async def build():
    await cppmake.cmake(
        name="xlnt",
        dir="./package/xlnt",
        args=[
            "-DSTATIC=true",
            "-DLIBRARY=true",
            "-DTESTS=false",
            "-DSAMPLES=false",
            "-DBENCHMARKS=false",
            "-DPYTHON=false",
            "-DDOCUMENTATION=false"
        ]
    )

"""
>>> cat ./package/xlnt/CMakeLists.txt | grep option
add_compile_options("$<$<C_COMPILER_ID:MSVC>:/utf-8>")
add_compile_options("$<$<CXX_COMPILER_ID:MSVC>:/utf-8>")
option(STATIC "Set to ON to build xlnt as a static library instead of a shared library" OFF)
option(LIBRARY "Set to ON to build the main XLNT library" ON)
option(TESTS "Set to ON to build test executable (in ./tests)" OFF)
option(SAMPLES "Set to ON to build executable code samples (in ./samples)" OFF)
option(BENCHMARKS "Set to ON to build performance benchmarks (in ./benchmarks)" OFF)
option(PYTHON "Set to ON to build Arrow conversion functions (in ./python)" OFF)
option(DOCUMENTATION "Set to ON to build API reference documentation (in ./api-reference)" OFF)
# Platform specific options
  option(STATIC_CRT "Link with the static version of MSVCRT (/MT[d])" OFF)
  option(COVERAGE "Generate coverage data using gcov" OFF)
  option(XLNT_ALL_WARNINGS_AS_ERRORS "Set to ON to convert all warnings into errors. This option is used during xlnt development/CI." OFF)
# Add components according to selected options
  option(XLNT_USE_LOCALE_COMMA_DECIMAL_SEPARATOR "Set to ON to enable unit tests and/or benchmarks that use a locale containing a comma as the decimal separator." OFF)
  option(XLNT_USE_LOCALE_ARABIC_DECIMAL_SEPARATOR "Set to ON to enable unit tests and/or benchmarks that use a locale containing the arabic decimal separator." OFF)
  # note the option ALL which allows to build the docs together with the application
"""