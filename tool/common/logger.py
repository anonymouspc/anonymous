import json
import os

class CompileCommandsLogger:
    def __init__(self):
        try:
            self.content = json.load(open("./bin/cache/compile_commands.json", 'r'))
        except:
            self.content = []
        os.makedirs("./bin/cache", exist_ok=True)
        self.writer = open("./bin/cache/compile_commands.json", 'w')

    def __del__(self):
        json.dump(self.content, self.writer, indent=4)

    def log(self, file, command):
        found = False
        for entry in self.content:
            if entry["file"] == file:
                entry["command"] = ' '.join(command)
                found = True

        if not found:
            self.content.append({
                "directory": os.path.abspath('.'),
                "file": file,
                "command": ' '.join(command)
            })

compile_commands_logger = CompileCommandsLogger()

class CompileOutputLogger:
    def __init__(self):
        os.makedirs("./bin/cache", exist_ok=True)
        self.writer = open("./bin/cache/compile_output.txt", 'w')
        self.logged = False

    def log(self, message):
        if not self.logged:
            self.writer.write(message)
            self.logged = True

compile_output_logger = CompileOutputLogger()

class ModuleMapperLogger:
    def __init__(self):
        os.makedirs("./bin/cache", exist_ok=True)
        self.writer = open("./bin/cache/module_mapper.txt", 'w')
    
    def log(self, name, file):
        self.writer.write(f"{name} {file}\n")
        self.writer.flush()

module_mapper_logger = ModuleMapperLogger()