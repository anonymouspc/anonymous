from cppmake.basic.config       import config
from cppmake.compiler.all       import compiler
from cppmake.system.all         import system
from cppmake.target.package     import Package
from cppmake.target.module      import Module
from cppmake.utility.algorithm  import recursive_find
from cppmake.utility.filesystem import exist_dir, remove_dir
from cppmake.utility.process    import run_process

async def cmake(name, dir, args=[]):
    package = await Package(name)
    try:
        if not exist_dir(package.build_dir):
            env=system.env.copy()
            env["CXX"] = compiler.name
            await run_process(
                command=[
                    "cmake",
                    "-S", dir,
                    "-B", package.build_dir,
                    f"-DCMAKE_PREFIX_PATH={';'.join(await recursive_find(await Module(name), navigates=["import_modules", "import_package"], target="install_dir"))}",
                    f"-DCMAKE_INSTALL_PREFIX={package.install_dir}",
                    f"-DCMAKE_INSTALL_LIBDIR=lib",
                    f"-DCMAKE_BUILD_TYPE={config.type}",
                    *args
                ],
                env=env
            )
    except:
        remove_dir(package.build_dir)
        raise
    try:
        await run_process(
            command=[
                "cmake",
                "--build", package.build_dir,
                "-j",      str(config.parallel)
            ], 
            print_stderr=False, 
        )
    except:
        raise
    try:
        await run_process(
            command=[
                "cmake",
                "--install", package.build_dir,
                "-j",        str(config.parallel)
            ],
            print_stderr=False, 
        )
    except:
        remove_dir(package.install_dir)
        raise