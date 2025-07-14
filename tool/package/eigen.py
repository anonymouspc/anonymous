from common.make import include

include(
    name="eigen",
    dir="./package/eigen"
)
include(
    name="eigen",
    dir="./package/eigen/unsupported"
)

# Hack
from common.config import type
import re
with open(f"./binary/{type}/package/eigen/install/include/Eigen/src/Core/util/Constants.h", 'r') as reader:
    content = reader.read()
    content = re.sub(r'^const', "inline const", content, flags=re.MULTILINE)
    with open(f"./binary/{type}/package/eigen/install/include/Eigen/src/Core/util/Constants.h", 'w') as writer:
        writer.write(content)