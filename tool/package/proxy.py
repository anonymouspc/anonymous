import shutil
from module.config import *

global_module = \
"""
module;
#undef in
#undef self
"""
with open("./package/proxy/include/proxy/v4/proxy.ixx", 'r') as reader, open("./module/proxy/v4.cpp", 'w') as writer:
    content = reader.read()
    content = content.replace("module;", global_module)
    writer.write(content)

shutil.copytree("./package/proxy/include", f"./bin/{type}/package/install/include", dirs_exist_ok=True)