from cppmake.utility.decorator  import member
from cppmake.utility.filesystem import absolute_path, create_dir
import json

class CompileCommandsLogger:
    def __init__   (self):                     ...
    def __del__    (self):                     ...
    def log_command(self, command, code_file): ...
    
compile_commands_logger = ...



@member(CompileCommandsLogger)
def __init__(self):
    create_dir("binary/cache")
    try:
        self._content = json.load(open("binary/cache/compile_commands.json", 'r'))
    except:
        self._content = []
    self._writer = open("binary/cache/compile_commands.json", 'w')

@member(CompileCommandsLogger)
def __del__(self):
    json.dump(self._content, self._writer, indent=4)

@member(CompileCommandsLogger)
def log_command(self, command, code_file):
    for entry in self._content:
        if entry["file"] == code_file:
            self._content.remove(entry)
    self._content.append({
        "directory": absolute_path('.'),
        "file"     : code_file,
        "command"  : ' '.join(command)
    })

compile_commands_logger = CompileCommandsLogger()
