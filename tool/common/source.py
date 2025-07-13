from common.algorithm import recursive_find
from common.compiler  import preprocess_file, compile_source
from common.config    import type, object_suffix
from common.module    import Module
from common.package   import Package
import os
import re
  
class Source:
    pool    = {}
    current = 0
    total   = 0

    def __new__(self, name):
        if name in Source.pool.keys():
            return Source.pool[name]
        else:
            self = super().__new__(self)
            Source.pool[name] = self

            # Info
            self.name        = name
            self.code_file   =            f"./source/{self.name.replace('.', '/').replace(':', '/')}.cpp"
            self.object_file = f"./binary/{type}/source/{self.name.replace('.', '.').replace(':', '-')}.{object_suffix}"
            self.content     = preprocess_file(code_file=self.code_file)

            # Import
            self.import_modules = []
            import_names = re.findall(r'^\s*import\s+([\w\.:]+)\s*;\s*$', self.content, flags=re.MULTILINE)
            for import_name in import_names:
                self.import_modules += [Module(name=import_name)]

            # Status
            self.is_compiled = all(module.is_compiled for module in self.import_modules)              and \
                               os.path.isfile(self.object_file)                                       and \
                               os.path.getmtime(self.code_file) <= os.path.getmtime(self.object_file)
            if not self.is_compiled:
                Source.total += 1

            # Return
            return self

    def compile(self):
        if not self.is_compiled:
            # Import
            for import_module in self.import_modules:
                import_module.compile()

            # Self
            Source.current += 1
            print(f"compile source [{Source.current}/{Source.total}]: {self.name}")
            compile_source(code_file   =self.code_file, 
                           include_dirs=recursive_find(node=self, func=lambda module: Package(module.name).include_dir if Package.exist(module.name) else None, root=False),
                           object_file =self.object_file)
            
            # Status
            self.is_compiled = True

    def __eq__(self, str):
        return self.name == str

