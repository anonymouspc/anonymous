from common.algorithm import recursive_find
from common.config    import type, module_suffix, object_suffix
from common.compiler  import preprocess_file, compile_module
from common.error     import BuildError
from common.package   import Package
import os
import re

class Module:
    pool    = {}
    current = 0
    total   = 0

    def __new__(self, name, from_modules=[]):
        if name in Module.pool.keys():
            return Module.pool[name]
        else:
            self = super().__new__(self)
            Module.pool[name] = self

            # Info
            self.name        = name
            self.code_file   =            f"./module/{self.name.replace('.', '/').replace(':', '/')}.cpp"
            self.module_file = f"./bin/{type}/module/{self.name.replace('.', '.').replace(':', '-')}.{module_suffix}"
            self.object_file = f"./bin/{type}/module/{self.name.replace('.', '.').replace(':', '-')}.{object_suffix}"
            self.content     = preprocess_file(code_file=self.code_file, name=self.name, module_file=self.module_file)

            # Import
            self.from_modules   = from_modules
            self.import_modules = []
            import_names = re.findall(r'^\s*(?:export\s+)?import\s+([\w\.:]+)\s*;\s*$', self.content, flags=re.MULTILINE)
            for import_name in import_names:
                if import_name.startswith(':'):
                    import_name = f"{self.name.partition(':')[0]}{import_name}"
                if import_name in self.from_modules:
                    raise BuildError(f"fatal error: module dependency circle {' -> '.join(module.name for module in self.from_modules + [self] + [Module(import_name)])}")
                self.import_modules += [Module(name=import_name, from_modules=self.from_modules + [self])]

            # Subtask
            if Package.exist(self.name):
                Package(self.name, by_module=self)

            # Status
            self.is_compiled = all(module.is_compiled for module in self.import_modules)              and \
                               (not Package.exist(self.name) or Package(self.name).is_built)          and \
                               os.path.isfile(self.module_file)                                       and \
                               os.path.getmtime(self.code_file) <= os.path.getmtime(self.module_file)
            if not self.is_compiled:
                Module.total += 1

            # Check
            if self.module_file is not None:
                export_names = re.findall(r'^\s*export\s+module\s+([\w\.:]+)\s*;\s*$', self.content, flags=re.MULTILINE)
                if (len(export_names) != 1 or export_names[0] != self.name):
                    raise BuildError(f"fatal error: file {self.code_file} should export module {self.name}")
                
            # Return
            return self

    def compile(self):
        if not self.is_compiled:
            # Import
            for import_module in self.import_modules:
                import_module.compile()

            # Subtask
            if Package.exist(self.name):
                Package(self.name).build()

            # Self
            Module.current += 1
            print(f"compile module [{Module.current}/{Module.total}]: {self.name}")
            compile_module(code_file   =self.code_file, 
                           include_dirs=recursive_find(node=self, func=lambda module: Package(module.name).include_dir if Package.exist(module.name) else None, root=True), 
                           module_file =self.module_file, 
                           object_file =self.object_file)
            
            # Status
            self.is_compiled = True

    def __eq__(self, str):
        return self.name == str