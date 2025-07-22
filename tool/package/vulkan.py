from common.config import argv, compiler
from common.error  import LogicError
from common.make   import include, lib
import common.config
import sys

async def initialize():
    if not argv.enable_vulkan:
        raise LogicError("arg `--disable-vulkan` set but package `vulkan` imported")
    if not hasattr(argv, "with_vulkan"):
        if sys.platform == "win32":
            raise LogicError("arg `--enable-vulkan` set but environment `--with-vulkan` not set and not default configurable")
        elif sys.platform == "linux" or sys.platform == "darwin":
            common.config.link_flags += ["-lvulkan"]
    common.config.define_flags["ENABLE_VULKAN"] = "true"

async def build():
    await include(
        name="vulkan",
        dir="./package/vulkan/vulkan"
    )
    await include(
        name="vulkan",
        dir="./package/vulkan/Vulkan-Headers/include"
    )
    if hasattr(argv, "with_vulkan"):
        await lib(
            name="vulkan",
            file=argv.with_vulkan
        )