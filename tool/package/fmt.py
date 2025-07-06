import shutil
from module.config import *

global_module = \
"""
module;
#undef in
#undef self
#define FMT_IMPORT_STD
#define FMT_HEADER_ONLY
#include <cstdlib>
#include <cstring>
"""
with open("./package/fmt/src/fmt.cc", 'r') as reader, open("./module/fmt.cpp", 'w') as writer:
    content = reader.read()
    content = content.replace("module;",                      global_module)
    content = content.replace('FMT_HAS_INCLUDE("format.cc")', "false"      )
    content = content.replace('FMT_HAS_INCLUDE("os.cc")',     "false"      )
    writer.write(content)

shutil.copytree("./package/fmt/include", f"./bin/{type}/package/install/include", dirs_exist_ok=True)    
