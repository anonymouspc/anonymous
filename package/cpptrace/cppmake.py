from cppmakelib import *

def build():
    cmake.build(
        package=package
    )

"""
>>> cat ./package/cpptrace/git/CMakeLists.txt | grep option
  add_compile_options(-fsanitize=address)
  add_link_options(-fsanitize=address)
  add_compile_options($<$<NOT:$<CXX_COMPILER_ID:MSVC>>:-g0>)
    src/options.cpp
    src/symbols/dwarf/dwarf_options.cpp
  warning_options
    warning_options
    ${warning_options}
target_compile_options(
  ${warning_options}
  target_compile_options(${target_name} PRIVATE -Wno-missing-field-initializers)
  # option(CPPTRACE_ADDR2LINE_SEARCH_SYSTEM_PATH "" OFF)
      target_compile_options(${target_name} PRIVATE ${LIBUNWIND_CFLAGS_OTHER})
      target_compile_options(${target_name} PRIVATE ${LIBUNWIND_CFLAGS_OTHER})
"""