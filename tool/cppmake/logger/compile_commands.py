from cppmake.utility.filesystem import absolute_path, create_dir
import json

class CompileCommandsLogger:
    def log(self, command, code_file):
        found = False
        for entry in self.content:
            if entry["file"] == code_file:
                entry["command"] = command
                found = True
        if not found:
            self.content.append({
                "directory": absolute_path('.'),
                "file": code_file,
                "command": ' '.join(command)
            })

    def __init__(self):
        create_dir("./bin/cache")
        try:
            self.content = json.load(open("./bin/cache/compile_commands.json", 'r'))
        except:
            self.content = []
        self.writer = open("./bin/cache/compile_commands.json", 'w')

    def __del__(self):
        json.dump(self.content, self.writer, indent=4)

compile_commands_logger = CompileCommandsLogger()
