from cppmake.basic.config       import config
from cppmake.system.all         import system
from cppmake.target.package     import Package
from cppmake.utility.filesystem import absolute_path, create_dir, remove_dir
from cppmake.utility.process    import run_process

async def autogen(name, file, args=[]):
    package = await Package(name)
    try:
        await run_process(
            command=[
                absolute_path(file),
                *args
            ]
        )
    except:
        remove_dir(package.build_dir)
        raise

async def configure(name, file, args=[]):
    package = await Package(name)
    try:
        env=system.env.copy()
        env["CXX"] = config.compiler
        create_dir(package.build_dir)
        await run_process(
            command=[
                absolute_path(file),
                f"--prefix={absolute_path(package.install_dir)}",
                f"--libdir={absolute_path(package.install_dir)}/lib",
                *args
            ],
            cwd=package.build_dir,
            env=env
        )
    except:
        remove_dir(package.build_dir)
        raise

async def make(name, dir, args=[]):
    package = await Package(name)
    try:
        await run_process(
            command=[
                "make",
                "-j", str(config.parallel),
                *args
            ],
            cwd=package.build_dir,
            print_stderr=False,
        )
    except:
        raise
    try:
        await run_process(
            command=[
                "make",
                "install",
                "-j", str(config.parallel)
            ],
            cwd=package.build_dir, 
            print_stderr=False, 
        )
    except:
        remove_dir(package.install_dir)
        raise
