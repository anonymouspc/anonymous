from common.algorithm import recursive_find
from common.config    import type, library_suffix, shared_suffix
import os

class Package:
    pool    = {}
    current = 0
    total   = 0

    def __new__(self, name, by_module=None):       
        name = name.partition('.')[0]

        if name in Package.pool.keys():
            Package.pool[name].by_modules += [by_module] if by_module is not None else []
            return Package.pool[name]
        else:
            self = super().__new__(self)
            self.by_modules = [by_module] if by_module is not None else []
            Package.pool[name] = self

            # Info
            self.name          = name
            self.package_file  = f"./tool/package/{self.name.replace('.', '/').replace(':', '/')}.py"
            self.install_dir   = None
            self.include_dir   = None
            self.library_files = None
            self.update()
            
            # Status
            self.is_configured = os.path.isdir(f"./binary/{type}/package/{self.name}/build")
            self.is_built      = os.path.isdir(f"./binary/{type}/package/{self.name}/install")
            self.is_installed  = (not os.path.isdir(f"./binary/{type}/package/{self.name}/install/include") or os.path.getmtime(f"./binary/{type}/package/{self.name}/install/include") < os.path.getmtime("./include")) and \
                                 (not os.path.isdir(f"./binary/{type}/package/{self.name}/install/lib"    ) or os.path.getmtime(f"./binary/{type}/package/{self.name}/install/lib"    ) < os.path.getmtime("./lib"    ))
            if not self.is_built:
                Package.total += 1

            # Check
            assert Package.exist(self.name)

            # Return
            return self
        
    def build(self, from_packages=[]):
        if not self.is_built:
            # Import 
            for by_module in self.by_modules:
                for import_package in recursive_find(node=by_module, func=lambda module: Package(module.name) if Package.exist(module.name) else None):
                    if import_package not in from_packages and import_package is not self:
                        import_package.build(from_packages=from_packages + [self])

            # Self
            Package.current += 1
            print(f"build package [{Package.current}/{Package.total}]: {self.name}")
            exec(f"from package.{self.name} import *")
            self.update()

            # Status
            self.is_built = True
        
    def exist(name):
        name = name.partition('.')[0]
        return os.path.isfile(f"./tool/package/{name}.py")
    
    def update(self):
        self.install_dir   =  f"./binary/{type}/package/{self.name}/install"         if os.path.isdir (f"./binary/{type}/package/{self.name}/install")         else None
        self.include_dir   =  f"./binary/{type}/package/{self.name}/install/include" if os.path.isdir (f"./binary/{type}/package/{self.name}/install/include") else None
        self.library_files = [f"./binary/{type}/package/{self.name}/install/lib/{file}"                                                                                                              \
                              for file in os.listdir    (f"./binary/{type}/package/{self.name}/install/lib")                                                                                         \
                              if          os.path.isfile(f"./binary/{type}/package/{self.name}/install/lib/{file}") and (file.endswith(f".{library_suffix}") or file.endswith(f".{shared_suffix}"))] \
                              if          os.path.isdir (f"./binary/{type}/package/{self.name}/install/lib") else None
                
    def __eq__(self, str):
        return self.name == str
    