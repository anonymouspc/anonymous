from common.algorithm import recursive_find
from common.compiler  import link_object
from common.config    import type, object_suffix, executable_suffix
from common.package   import Package
from common.source    import Source
import os

class Object:
    pool    = {}
    current = 0
    total   = 0
    
    def __new__(self, name):
        if name in Object.pool.keys():
            return Object.pool[name]
        else:
            self = super().__new__(self)
            Object.pool[name] = self

            # Info
            self.name            = name
            self.object_file     = f"./bin/{type}/module/{self.name.replace(':', '-')}.{object_suffix}"
            self.executable_file = f"./bin/{type}/{self.name.replace('.', '/', 1)}.{executable_suffix}" if executable_suffix != "" else f"./bin/{type}/{self.name.replace('.', '/', 1)}"

            # Subtask
            Source(self.name)

            # Status
            self.is_linked = Source(self.name).is_compiled                                                and \
                                os.path.isfile(self.object_file)                                             and \
                                os.path.isfile(self.executable_file)                                         and \
                                os.path.getmtime(self.object_file) <= os.path.getmtime(self.executable_file)
            if not self.is_linked:
                Object.total += 1

            # Return
            return self

    def link(self):
        if not self.is_linked:
            # Subtask
            Source(self.name).compile()

            # Self
            Object.current += 1
            print(f"link object [{Object.current}/{Object.total}]: {self.name}")
            link_object(object_files   =recursive_find(node=Source(self.name), func=lambda source_or_module: source_or_module.object_file,                                     root=True               ),
                        library_files  =recursive_find(node=Source(self.name), func=lambda module: Package(module.name).library_files if Package.exist(module.name) else None, root=False, flatten=True),
                        executable_file=self.executable_file)
            
            # Status
            self.is_linked = True
