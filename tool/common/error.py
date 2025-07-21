class Error(Exception):
    def add_prefix(self, prefix):
        super().__init__(f"{prefix}\n{self}")
        return self

class LogicError(Exception):
    pass

class SubprocessError(Exception):
    def __init__(self, message, is_stderr_printed):
        super().__init__(message)
        self.is_stderr_printed = is_stderr_printed

