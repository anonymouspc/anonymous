import json
import os

class CompileCommandsLogger:
    def __init__(self):
        try:
            self.content = json.load(open("./bin/cache/compile_commands.json", 'r'))
        except json.decoder.JSONDecodeError:
            self.content = []
        self.writer = open("./bin/cache/compile_commands.json", 'w')

    def __del__(self):
        json.dump(self.content, self.writer, indent=4)

    def log(self, file, command):
        found = False
        for entry in self.content:
            if entry["file"] == file:
                entry["command"] = command
                found = True

        if not found:
            self.content.append({
                "directory": os.path.abspath('.'),
                "file": file,
                "command": command
            })

compile_commands_logger = CompileCommandsLogger()

class CompileOutputLogger:
    def __init__(self):
        self.writer = open("./bin/cache/compile_output.txt", 'w')

    def log(self, message):
        self.writer.write(message)

compile_output_logger = CompileOutputLogger()

class ModuleMapperLogger:
    def __init__(self):
        self.writer = open("./bin/cache/module_mapper.txt", 'w')
    
    def log(self, name, file):
        self.writer.write(f"{name} {file}\n")

module_mapper_logger = ModuleMapperLogger()