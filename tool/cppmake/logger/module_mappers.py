from cppmake.utility.filesystem import create_dir

class ModuleMappersLogger:
    def __init__(self):
        create_dir("./binary/cache")
        self.writer = open("./binary/cache/module_mappers.txt", 'w')

    def log(self, module_name, module_file):
        self.writer.write(f"{module_name} {module_file}\n")
        self.writer.flush()

module_mappers_logger = ModuleMappersLogger()