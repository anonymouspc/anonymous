from cppmake.basic.config       import config
from cppmake.builder.git        import git
from cppmake.system.all         import system
from cppmake.utility.decorator  import member, syncable
from cppmake.utility.filesystem import exist_dir, create_dir
import json
import time

class PackageStatusLogger:
    def __init__(self):                        ...
    def             log_status(self, package): ...
    async def async_log_status(self, package): ...
    def             get_status(self, package): ...
    async def async_get_status(self, package): ...

package_status_logger = ...


@member(PackageStatusLogger)
def __init__(self):
    create_dir(f"binary/{config.type}/cache")
    try:
        self._content = json.load(open(f"binary/{config.type}/cache/package_status.json", 'r'))
    except:
        self._content = {}
    self._writer = open(f"binary/{config.type}/cache/package_status.json", 'w')

@member(PackageStatusLogger)
@syncable
async def async_log_status(self, package):
    self._content[package.name] = {
        "time"      : time.time(),
        "env"       : system.env,
        "compiler"  : config.compiler,
        "std"       : config.std,      
        "git_log"   : await git.async_log   (git_dir=package.git_dir) if exist_dir(package.git_dir) else None,
        "git_status": await git.async_status(git_dir=package.git_dir) if exist_dir(package.git_dir) else None
    }

@member(PackageStatusLogger)
@syncable
async def async_get_status(self, package):
    return package.name in self._content.keys()                                                                                                   and \
           system.env      == self._content[package.name]["env"]                                                                                  and \
           config.compiler == self._content[package.name]["compiler"]                                                                             and \
           config.std      == self._content[package.name]["std"]                                                                                  and \
           (await git.async_log   (git_dir=package.git_dir) == self._content[package.name]["git_log"]    if exist_dir(package.git_dir) else True) and \
           (await git.asnyc_status(git_dir=package.git_dir) == self._content[package.name]["git_status"] if exist_dir(package.git_dir) else True)

package_status_logger = PackageStatusLogger()