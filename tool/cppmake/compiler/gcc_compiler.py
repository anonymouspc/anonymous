from cppmake.basic.config import argv
from cppmake.utility

class GccCompiler:
    def __init__(self):
        self.compile_flags = []
        self.link_flags = []
    
    def preprocess_file(self):
        return 

    def compile_module(self, module_only=False):
        pass

    def compile_source(self, target=argv.target):
        pass

    