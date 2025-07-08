import re
import shutil
from module.config import *

shutil.copytree("./package/eigen/Eigen",       f"./bin/{type}/package/install/include/Eigen",       dirs_exist_ok=True)
shutil.copytree("./package/eigen/unsupported", f"./bin/{type}/package/install/include/unsupported", dirs_exist_ok=True)

with open(f"./bin/{type}/package/install/include/Eigen/src/Core/util/Constants.h", 'r') as reader:
    content = reader.read()
    content = re.sub(r'^const', "inline const", content, flags=re.MULTILINE)
    with open(f"./bin/{type}/package/install/include/Eigen/src/Core/util/Constants.h", 'w') as writer:
        writer.write(content)