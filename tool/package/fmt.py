from common.make import include, module

include(
    name="fmt",
    dir="./package/fmt/include"
)
module(
    name="fmt",
    file="./package/fmt/src/fmt.cc",
    replace={
        "module;": 
            """
            module;
            #define FMT_HEADER_ONLY
            #define FMT_IMPORT_STD
            #ifdef __clang__
                #pragma clang diagnostic ignored "-Winclude-angled-in-module-purview"
            #endif
            """,
        'FMT_HAS_INCLUDE("format.cc")': "false",
        'FMT_HAS_INCLUDE("os.cc")'    : "false"
    }
)
