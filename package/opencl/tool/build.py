import cppmake

if cppmake.system.name == "macos":
    cppmake.compiler.link_flags += ["-framework OpenCL"]

async def build():
    await cppmake.include(
        name="opencl",
        dir="./package/opencl/CL",
        relpath="CL"
    )
    if cppmake.system.name == "windows":
        await cppmake.lib(
            name="opencl",
            file="C:/Windows/System32/OpenCL.dll"
        )
    elif cppmake.system.name == "linux":
        await cppmake.lib(
            name="opencl",
            file="/usr/lib/libOpenCL.so"
        )