from cppmake.utility.filesystem import create_dir

class ModuleMappersLogger:
    def log(self, name, module_file):
        self.writer.write(f"{name} {module_file}\n")
        self.writer.flush()

    def __init__(self):
        create_dir("./binary/cache")
        self.writer = open("./binary/cache/module_mappers.txt", 'w')

module_mappers_logger = ModuleMappersLogger()