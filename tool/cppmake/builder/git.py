from cppmake.error.config      import ConfigError
from cppmake.error.subprocess  import SubprocessError
from cppmake.execution.run     import async_run
from cppmake.utility.decorator import member, syncable

class Git:
    name = "git"
    path = "git"
    def           __init__ (self):          ...
    async def     __ainit__(self):          ...
    def             log    (self, git_dir): ...
    async def async_log    (self, git_dir): ...
    def             status (self, git_dir): ...
    async def async_status (self, git_dir): ...

git = ...



@member(Git)
@syncable
async def __ainit__(self):
    await Git._async_check()

@member(Git)
@syncable
async def async_log(self, git_dir):
    return await async_run(
        command=[
            self.path,
            "-C", git_dir,
            "log", "-1", "--format=%H"
        ],
        return_stdout=True
    )

@member(Git)
@syncable
async def async_status(self, git_dir):
    return await async_run(
        command=[
            self.path,
            "-C", git_dir,
            "status", "--short"
        ]
    )

@member(Git)
async def _async_check():
    try:
        try:
            version = await async_run(command=[Git.path, "--version"], return_stdout=True)
        except TypeError as e:
            print(e)
            print(type(async_run))
            print('='*30)
            exit(-1)
        
        if "git" not in version.lower():
            raise ConfigError(f'"git" is not installed (with "{Git.path} --version" outputs "{version.replace('\n', ' ')}")')
    except SubprocessError as e:
        raise ConfigError(f'"git" is not installed (with "{Git.path} --version" exits {e.code}')
        
git = Git()