from cppmake.compiler.all        import compiler
from cppmake.error.logic         import LogicError
from cppmake.utility.filesystem  import modified_time_of_file
import json
import re
import time

class ModuleDependenciesLogger:
    async def get(self, name, code_file):
        if name in self.content.keys() and modified_time_of_file(code_file) < self.content[name]["time"]:
            return self.content[name]["dependencies"]
        else:
            await compiler.preprocess_code(code_file)
            import_names = [import_name if not import_name.startswith(':') else f"{name.split(':')[0]}{import_name}" for import_name in re.findall(r'^\s*(?:export\s+)?import\s+([\w\.:]+)\s*;\s*$', code, flags=re.MULTILINE)]
            self.content[name] = {
                "time": time.time(),
                "dependencies": import_names
            }
            return import_names
        
    def __init__(self):
        try:
            self.content = json.load(open("./binary/cache/module_dependencies.json", 'r'))
        except:
            self.content = {}
        self.writer = open("./binary/cache/module_dependencies.json", 'w')

    def __del__(self):
        json.dump(self.content, self.writer, indent=4)

module_dependencies_logger = ModuleDependenciesLogger()