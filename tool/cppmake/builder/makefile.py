from cppmake.basic.config       import config
from cppmake.compiler.all       import compiler
from cppmake.error.config       import ConfigError
from cppmake.error.subprocess   import SubprocessError
from cppmake.execution.run      import async_run
from cppmake.system.all         import system
from cppmake.utility.decorator  import member, syncable
from cppmake.utility.filesystem import absolute_path, create_dir, remove_dir

class Makefile:
    name = "makefile"
    path = "make"
    def           __init__   (self):                                     ...
    async def     __ainit__  (self):                                     ...
    def             configure(self, package, file="configure", args=[]): ...
    async def async_configure(self, package, file="configure", args=[]): ...
    def             build    (self, package,                   args=[]): ...
    async def async_build    (self, package,                   args=[]): ...
    def             install  (self, package,                   args=[]): ...
    async def async_install  (self, package,                   args=[]): ...

makefile = ...



@member(Makefile)
@syncable
async def __ainit__(self):
    await Makefile._async_check()

@member(Makefile)
@syncable
async def async_configure(self, package, file="configure", args=[]):
    try:
        create_dir(package.build_dir)
        env = system.env.copy()
        env["CXX"] = compiler.path
        await async_run(
            command=[
           f"{package.git_dir}/{file}",
           f"--prefix={absolute_path(package.install_dir)}",
           f"--libdir={absolute_path(package.install_dir)}/lib"
            *args
            ],
            cwd=package.build_dir,
            env=env
        )
    except:
        remove_dir(package.build_dir)
        raise

@member(Makefile)
@syncable
async def async_build(self, package, args=[]):
    await async_run(
        command=[
            self.path,
            "-C", package.build_dir,
            "-j", str(config.parallel),
           *args
        ]
    )

@member(Makefile)
@syncable
async def async_install(self, package, args=[]):
    try:
        create_dir(package.install_dir)
        await async_run(
            command=[
                self.path, "install"
                "-C", package.build_dir,
                "-j", str(config.parallel),
               *args 
            ]
        )
    except:
        remove_dir(package.install_dir)
        raise

@member(Makefile)
async def _async_check():
    try:
        version = await async_run(command=[Makefile.path, "--version"], return_stdout=True)
        if "make" not in version.lower():
            raise ConfigError(f'"makefile" is not installed (with f"{Makefile.path} --version" outputs "{version.replace('\n', ' ')}")')
    except SubprocessError as e:
        raise ConfigError(f'"makefile" is not installed (with f"{Makefile.path} --version" exits {e.code}')
        
makefile = Makefile()