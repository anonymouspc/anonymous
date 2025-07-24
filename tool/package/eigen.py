from common.make  import include
from file.package import Package
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

    package = await Package("eigen")
    with open(f"{package.include_dir}/Eigen/src/Core/util/Constants.h", 'r') as reader:
        content = reader.read()
        content = re.sub(r'^const', "inline const", content, flags=re.MULTILINE)
    with open(f"{package.include_dir}/Eigen/src/Core/util/Constants.h", 'w') as writer:
        writer.write(content)