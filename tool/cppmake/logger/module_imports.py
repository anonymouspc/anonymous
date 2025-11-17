from cppmake.basic.config        import config
from cppmake.basic.main          import on_exit
from cppmake.compiler.all        import compiler
from cppmake.error.logic         import LogicError
from cppmake.execution.operation import when_all
from cppmake.file.file_system    import create_dir, modified_time_of_file, iterate_dir
from cppmake.utility.algorithm   import recursive_collect
from cppmake.utility.decorator   import member, once, syncable
import json
import re
import time

class ModuleImportsLogger:
    def           __init__      (self):         ...
    def           __exit__      (self):         ...
    def             get_imports (self, module): ...
    async def async_get_imports (self, module): ...

module_imports_logger = ...



@member(ModuleImportsLogger)
def __init__(self):
    create_dir(f"binary/{config.type}/cache")
    try:
        self._content = json.load(open(f"binary/{config.type}/cache/module_imports.json", 'r'))
    except:
        self._content = {
            "module": {},
            "source": {}
        }
    on_exit(self.__exit__)

@member(ModuleImportsLogger)
def __exit__(self):
    json.dump(self._content, open(f"binary/{config.type}/cache/module_imports.json", 'w'), indent=4)

@member(ModuleImportsLogger)
@syncable
async def async_get_imports(self, unit):
    from cppmake.unit.module import Module
    if                        unit.name not in self._content[type(unit).__qualname__.lower()].keys() or \
       modified_time_of_file(unit.code_file) > self._content[type(unit).__qualname__.lower()][unit.name]["time"]:
        try:
            code = open(unit.code_file, 'r').read()
        except FileNotFoundError:
            raise LogicError(f"{type(unit).__qualname__.lower()} {unit.name} not found (with file = {unit.code_file})")
        code = re.sub(r'^\s*#\s*include(?!\s*<version>).*$', "", code, flags=re.MULTILINE)
        preprocessed = await compiler.async_preprocess(code=code)
        if type(unit) == Module:
            exports = re.findall(r'^\s*export\s+module\s+([\w\.:]+)\s*;\s*$', preprocessed, flags=re.MULTILINE)
            if len(exports) != 1 or unit.name != exports[0]:
                raise LogicError(f"module {unit.name} has invalid export declarations (with file = {unit.code_file})")
        imports = re.findall(r'^\s*(?:export\s+)?import\s+([\w\.:]+)\s*;\s*$', preprocessed, flags=re.MULTILINE)
        imports = [import_ if not import_.startswith(':') else f"{unit.name.partition(':')[0]}{import_}" for import_ in imports]
        self._content[type(unit).__qualname__.lower()][unit.name] = {
            "time"   : time.time(),
            "imports": imports
        }
    return self._content[type(unit).__qualname__.lower()][unit.name]["imports"]
    
module_imports_logger = ModuleImportsLogger()