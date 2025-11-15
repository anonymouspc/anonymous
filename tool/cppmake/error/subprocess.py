import sys

class SubprocessError(Exception):
    def __init__(self, code, stderr, is_stderr_printed):
        super().__init__(stderr)
        self.code = code
        self.is_stderr_printed = is_stderr_printed

    def at_exit(self):
        if not self.is_stderr_printed:
            print(self, file=sys.stderr)