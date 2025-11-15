import sys

class LogicError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.prefixes = []

    def add_prefix(self, prefix):
        self.prefixes += [prefix]
        return self
    
    def at_exit(self):
        print(f"{'\n'.join(self.prefixes)}\nerror: {self}", file=sys.stderr)