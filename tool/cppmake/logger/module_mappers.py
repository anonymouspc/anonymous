from cppmake.basic.config       import config
from cppmake.utility.filesystem import create_dir
from cppmake.utility.decorator  import member

class ModuleMappersLogger:
    def __init__  (self):                  ...
    def log_mapper(self, module):          ...
    def get_mapper(self, *args, **kwargs): ...

module_mappers_logger = ...



@member(ModuleMappersLogger)
def __init__(self):
    create_dir(f"binary/{config.type}/cache")
    self._writer = open(f"binary/{config.type}/cache/module_mappers.txt", 'w')

@member(ModuleMappersLogger)
def log_mapper(self, module):
    self._writer.write(f"{module.name} {module.code_file}\n")
    self._writer.flush()

@member(ModuleMappersLogger)
def get_mapper(self, *args, **kwargs):
    return f"binary/{config.type}/cache/module_mapper.txt"

module_mappers_logger = ModuleMappersLogger()