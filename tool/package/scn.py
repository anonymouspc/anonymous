from common.make import cmake, module
  
async def build():
    await cmake(
        name="scn",
        dir="./package/scn",
        args=[
            "-DSCN_TESTS=false",
            "-DSCN_DOCS=false",
            "-DSCN_EXAMPLES=false",
            "-DSCN_BENCHMARKS=false",
          # "-DSCN_DISABLE_FAST_FLOAT=true" TODO: =false when clang++ supports charconv.float
        ]
    )
    await module(
        name="scn",
        file="./package/scn/src/scn/scn.cppm",
        replace={"module;": "module;\n#include <iterator>\nimport std;"}
    )

"""
>>> cat ./package/scnlib/cmake/options.cmake | grep option
option(SCN_CI "Enable CI preset" OFF)
option(SCN_TESTS "Enable tests" ${SCN_ENABLE_TESTS})
option(SCN_DOCS "Enable docs target" ${SCN_ENABLE_EXTRAS})
option(SCN_EXAMPLES "Enable examples target" ${SCN_ENABLE_EXTRAS})
option(SCN_INSTALL "Enable install target" ${SCN_ENABLE_EXTRAS})
option(SCN_HEADERS_AS_SYSTEM "Expose scn headers by marking them as SYSTEM" OFF)
option(SCN_MODULES "Enable C++20 module target (scn::module), requires CMake 3.28 and Ninja" OFF)
option(SCN_BENCHMARKS "Enable runtime benchmarks" ${SCN_ENABLE_EXTRAS})
option(SCN_BENCHMARKS_BUILDTIME "Enable buildtime benchmarks" ${SCN_ENABLE_EXTRAS})
option(SCN_BENCHMARKS_BINARYSIZE "Enable binary size benchmarks" ${SCN_ENABLE_EXTRAS})
option(SCN_COVERAGE "Enable coverage reporting" OFF)
option(SCN_TESTS_LOCALIZED "Enable localized tests (requires en_US.UTF-8 and fi_FI.UTF-8 locales)" OFF)
option(SCN_FUZZING "Enable fuzz tests (clang only)" OFF)
option(SCN_PEDANTIC "Enable pedantic compilation flags" ${SCN_ENABLE_EXTRAS})
option(SCN_WERROR "Halt compilation in case of a warning" ${SCN_CI})
option(SCN_DISABLE_REGEX "Disable regex support" OFF)
option(SCN_REGEX_BOOST_USE_ICU "Use ICU with the regex backend (Boost SCN_REGEX_BACKEND only)" OFF)
option(SCN_DISABLE_FAST_FLOAT "Disable the external dependency on fast_float, requires std::from_chars for floats" OFF)
option(SCN_USE_EXTERNAL_FAST_FLOAT "Use find_package for fast_float, instead of FetchContent" OFF)
option(SCN_USE_EXTERNAL_GTEST "Use find_package for GTest, instead of FetchContent" OFF)
option(SCN_USE_EXTERNAL_BENCHMARK "Use find_package for Benchmark, instead of FetchContent" OFF)
option(SCN_USE_EXTERNAL_REGEX_BACKEND "Use find_package for SCN_REGEX_BACKEND, instead of FetchContent" ON)
option(SCN_USE_32BIT "Compile as 32-bit (gcc or clang only)" OFF)
option(SCN_USE_EXCEPTIONS "Compile with exception support (disabling will cause test failures)" ON)
option(SCN_USE_RTTI "Compile with RTTI (run-time argv.type information) support" ON)
option(SCN_USE_NATIVE_ARCH "Add -march=native to build flags (gcc or clang only)" OFF)
option(SCN_USE_HASWELL_ARCH "Add -march=haswell to build flags (gcc or clang only)" OFF)
option(SCN_USE_ASAN "Compile with AddressSanitizer" OFF)
option(SCN_USE_UBSAN "Compile with UndefinedBehaviorSanitizer" OFF)
option(SCN_USE_MSAN "Compile with MemorySanitizer" OFF)
option(SCN_USE_STACK_PROTECT "Compile with various stack protection measures (gcc or clang only)" OFF)
option(SCN_USE_SAFESTACK "Compile with SafeStack (clang only, requires STACK_PROTECT, disallows ASAN)" OFF)
option(SCN_DISABLE_TYPE_SCHAR "Disable scanning of signed char" OFF)
option(SCN_DISABLE_TYPE_SHORT "Disable scanning of short" OFF)
option(SCN_DISABLE_TYPE_INT "Disable scanning of int" OFF)
option(SCN_DISABLE_TYPE_LONG "Disable scanning of long" OFF)
option(SCN_DISABLE_TYPE_LONG_LONG "Disable scanning of long long" OFF)
option(SCN_DISABLE_TYPE_INT128 "Disable scanning of int128" OFF)
option(SCN_DISABLE_TYPE_UCHAR "Disable scanning of unsigned char" OFF)
option(SCN_DISABLE_TYPE_USHORT "Disable scanning of unsigned short" OFF)
option(SCN_DISABLE_TYPE_UINT "Disable scanning of unsigned int" OFF)
option(SCN_DISABLE_TYPE_ULONG "Disable scanning of unsigned long" OFF)
option(SCN_DISABLE_TYPE_ULONG_LONG "Disable scanning of unsigned long long" OFF)
option(SCN_DISABLE_TYPE_UINT128 "Disable scanning of uint128" OFF)
option(SCN_DISABLE_TYPE_POINTER "Disable scanning of pointers (void*)" OFF)
option(SCN_DISABLE_TYPE_BOOL "Disable scanning of bool" OFF)
option(SCN_DISABLE_TYPE_CHAR "Disable scanning of char/wchar_t" OFF)
option(SCN_DISABLE_TYPE_CHAR32 "Disable scanning of char32_t " OFF)
option(SCN_DISABLE_TYPE_FLOAT "Disable scanning of float" OFF)
option(SCN_DISABLE_TYPE_DOUBLE "Disable scanning of double" OFF)
option(SCN_DISABLE_TYPE_LONG_DOUBLE "Disable scanning of long double" OFF)
option(SCN_DISABLE_TYPE_FLOAT16 "Disable scanning of std::float16_t" OFF)
option(SCN_DISABLE_TYPE_FLOAT32 "Disable scanning of std::float32_t" OFF)
option(SCN_DISABLE_TYPE_FLOAT64 "Disable scanning of std::float64_t" OFF)
option(SCN_DISABLE_TYPE_FLOAT128 "Disable scanning of std::float128_t" OFF)
option(SCN_DISABLE_TYPE_BFLOAT16 "Disable scanning of std::bfloat16_t" OFF)
option(SCN_DISABLE_TYPE_STRING "Disable scanning of std::basic_string" OFF)
option(SCN_DISABLE_TYPE_STRING_VIEW "Disable scanning of std::basic_string_view" OFF)
option(SCN_DISABLE_TYPE_CUSTOM "Disable scanning of user types" OFF)
option(SCN_DISABLE_IOSTREAM "Disable iostreams" OFF)
option(SCN_DISABLE_LOCALE "Disable all localization" OFF)
option(SCN_DISABLE_STRTOD "Disallow falling back on std::strtod when scanning floating-point values" OFF)
option(SCN_DISABLE_CHRONO "Disable <chrono> and <ctime> scanners" OFF)
option(SCN_DISABLE_FROM_CHARS "Disallow falling back on std::from_chars when scanning floating-point values" OFF)
option(SCN_DISABLE_STRTOD "Disallow falling back on std::strtod when scanning floating-point values" OFF)
"""