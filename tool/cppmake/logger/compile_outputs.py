from cppmake.utility.filesystem import create_dir

class CompileOutputsLogger:
    def log(self, message):
        if not self.logged:
            self.writer.write(message)
            self.logged = True

    def __init__(self):
        create_dir("./bin/cache")
        self.writer = open("./bin/cache/compile_outputs.txt", 'w')
        self.logged = False

compile_outputs_logger = CompileOutputsLogger()