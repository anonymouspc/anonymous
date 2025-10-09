import cppmake

if cppmake.system.name == "macos":
    cppmake.compiler.link_flags += ["-framework OpenGL"]

async def build():
    await cppmake.include(
        name="opencl",
        dir="./package/opengl/api",
    )
    if cppmake.system.name == "windows":
        await cppmake.lib(
            name="opengl",
            file="C:/Windows/System32/OpenGL.dll"
        )
    elif cppmake.system.name == "linux":
        await cppmake.lib(
            name="opengl",
            file="/usr/lib/libOpenGL.so"
        )