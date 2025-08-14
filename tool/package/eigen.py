from common.make  import include
from file.package import Package
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

    package = await Package("eigen")
    for root, _, files in os.walk(package.include_dir):
        for file in files:
            try:
                with open(f"{root}/{file}", 'r') as reader:
                    content = reader.read()
                    content = re.sub(r'^(const|constexpr) (?=[^\(\)]*;\s*$)', "inline constexpr ", content, flags=re.MULTILINE)
                with open(f"{root}/{file}", 'w') as writer:
                    writer.write(content)
            except UnicodeDecodeError:
                pass