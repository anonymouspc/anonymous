from cppmake.utility.filesystem import create_dir

class CompileOutputsLogger:
    def log(self, message):
        if not self.logged:
            self.writer.write(message)
            self.logged = True

    def __init__(self):
        create_dir("./binary/cache")
        self.writer = open("./binary/cache/compile_outputs.txt", 'w')
        self.logged = False

compile_outputs_logger = CompileOutputsLogger()