from cppmake.basic.config        import config
from cppmake.compiler.all        import compiler
from cppmake.error.logic         import LogicError
from cppmake.execution.operation import when_all
from cppmake.utility.decorator   import member, syncable
from cppmake.utility.filesystem  import create_dir, modified_time_of_file
import json
import re
import time

class UnitImportsLogger:
    def           __init__      (self):       ...
    def           __del__       (self):       ...
    def             get_imports (self, unit): ...
    async def async_get_imports (self, unit): ...
    def             peek_imports(self, name): ...
    async def async_peek_imports(self, name): ...

unit_imports_logger = ...



@member(UnitImportsLogger)
def __init__(self):
    create_dir(f"binary/{config.type}/cache")
    try:
        self._content = json.load(open(f"binary/{config.type}/cache/unit_imports.json", 'r'))
    except:
        self._content = {}
    self._writer = open(f"binary/{config.type}/cache/unit_imports.json", 'w')

@member(UnitImportsLogger)
def __del__(self):
    json.dump(self._content, self._writer, indent=4)

@member(UnitImportsLogger)
@syncable
async def async_get_imports(self, unit):
    from cppmake.unit.module import Module
    await self._async_log_imports(type=type(unit), name=unit.name, code_file=unit.code_file)
    return await when_all([Module.__anew__(import_) for import_ in self._content[f"{type(unit).__qualname__.lower()}/{unit.name}"]["imports"]])

@member(UnitImportsLogger)
@syncable
async def async_peek_imports(self, name):
    from cppmake.unit.module import Module
    await self._async_log_imports(type=Module, name=name, code_file=Module.name_to_file(name))
    return self._content[f"module/{name}"]["imports"]

@member(UnitImportsLogger)
async def _async_log_imports(self, type, name, code_file):
    from cppmake.unit.module import Module
    if               f"{type.__qualname__.lower()}/{name}" not in self._content.keys() or \
       self._content[f"{type.__qualname__.lower()}/{name}"]["time"] < modified_time_of_file(code_file):
        preprocessed = await compiler.async_preprocess(code_file=code_file)
        if type == Module:
            exports = re.findall(r'^\s*export\s+module\s+([\w\.:]+)\s*;\s*$', preprocessed, flags=re.MULTILINE)
            if len(exports) != 1 or name != exports[0]:
                raise LogicError(f"ambiguous module export: {name}, {exports}")
        imports = re.findall(r'^\s*(?:export\s+)?import\s+([\w\.:]+)\s*;\s*$', preprocessed, flags=re.MULTILINE)
        self._content[f"{type.__qualname__.lower()}/{name}"] = {
            "time"   : time.time(),
            "imports": imports
        }

unit_imports_logger = UnitImportsLogger()