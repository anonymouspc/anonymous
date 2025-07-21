from common.config import argv
from common.make   import include
import os
import re

async def build():
    await include(
        name="eigen",
        dir="./package/eigen"
    )
    await include(
        name="eigen",
        dir="./package/eigen/unsupported"
    )

    with open(f"./bin/{argv.type}/package/eigen/install/include/Eigen/src/Core/util/Constants.h", 'r') as reader:
        content = reader.read()
        content = re.sub(r'^const', "inline const", content, flags=re.MULTILINE)
    with open(f"./bin/{argv.type}/package/eigen/install/include/Eigen/src/Core/util/Constants.h", 'w') as writer:
        writer.write(content)
    os.utime (f"./bin/{argv.type}/package/eigen/install/include/Eigen/src/Core/util/Constants.h", 
             (os.path.getatime           ("./package/eigen/Eigen/src/Core/util/Constants.h"),
              os.path.getmtime           ("./package/eigen/Eigen/src/Core/util/Constants.h")))