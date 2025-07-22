from common.make  import include
from file.package import Package
import os
import re

async def build():
    await include(
        name="stdexec",
        dir="./package/stdexec/include"
    )

    package = await Package("stdexec")
    count = 0
    for root, _, files in os.walk(package.include_dir):
        for file in files:
            with open(f"{root}/{file}", 'r') as reader:
                content = reader.read()
                content = re.sub(r'namespace\s*{', f"inline namespace __{count}__ {{", content)
                count += 1
            with open(f"{root}/{file}", 'w') as writer:
                writer.write(content)