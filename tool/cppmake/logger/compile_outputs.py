from cppmake.file.file_system  import create_dir
from cppmake.utility.decorator import member

class CompileOutputsLogger:
    def __init__  (self):         ...
    def log_output(self, output): ...

compile_outputs_logger = ...



@member(CompileOutputsLogger)
def __init__(self):
    create_dir("binary/cache")
    self._writer = open("binary/cache/compile_outputs.txt", 'w')
    self._logged = False

@member(CompileOutputsLogger)
def log_output(self, output):
    if not self._logged:
        self._writer.write(output)
        self._logged = True

compile_outputs_logger = CompileOutputsLogger()