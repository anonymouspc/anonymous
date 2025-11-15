from cppmake.basic.config       import config
from cppmake.error.config       import ConfigError
from cppmake.error.subprocess   import SubprocessError
from cppmake.execution.run      import async_run
from cppmake.utility.algorithm  import recursive_collect
from cppmake.utility.decorator  import member, syncable
from cppmake.utility.filesystem import create_dir, remove_dir

class Cmake:
    name = "cmake"
    path = "cmake"
    def           __init__   (self):                            ...
    async def    __ainit__   (self):                            ...
    def             configure(self, package, dir=".", args=[]): ...
    async def async_configure(self, package, dir=".", args=[]): ...
    def             build    (self, package,          args=[]): ...
    async def async_build    (self, package,          args=[]): ...
    def             install  (self, package,          args=[]): ...
    async def async_install  (self, package,          args=[]): ...

cmake = ...



@member(Cmake)
@syncable
async def __ainit__(self):
    await Cmake._async_check()

@member(Cmake)
@syncable
async def async_configure(self, package, args=[]):
    try:
        create_dir(package.build_dir)
        await async_run(
            command=[
                self.path,
                "-S", package.git_dir,
                "-B", package.build_dir,
               f"-DCMAKE_BUILD_TYPE={config.type}",
               f"-DCMAKE_PREFIX_PATH={';'.join(recursive_collect(package, next=lambda package: package.import_packages, collect=lambda package: package.install_dir, on_root=False))}",
               f"-DCMAKE_INSTALL_PREFIX={package.install_dir}",
                "-DCMAKE_INSTALL_LIBDIR=lib",
               *args
            ]
        )
    except:
        remove_dir(package.build_dir)
        raise

@member(Cmake)
@syncable
async def async_build(self, package, args=[]):
    await async_run(
        command=[
            self.path,
            "--build", package.build_dir,
            "-j",      str(config.parallel),
           *args
        ]
    )

@member(Cmake)
@syncable
async def async_install(self, package, args=[]):
    try:
        create_dir(package.install_dir)
        await async_run(
            command=[
                self.path,
                "--install", package.build_dir,
                "-j",        str(config.parallel),
               *args
            ]
        )
    except:
        remove_dir(package.install_dir)
        raise

@member(Cmake)
async def _async_check():
    try:
        version = await async_run(command=[Cmake.path, "--version"], return_stdout=True)
        if "cmake" not in version.lower():
            raise ConfigError(f'"cmake" is not installed (with "{Cmake.path} --version" outputs "{version.replace('\n', ' ')}")')
    except SubprocessError as e:
        raise ConfigError(f'"cmake" is not found (with "{Cmake.path} --version" exits {e.code}')
        
cmake = ...
