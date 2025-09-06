class ProcessError(Exception):
    def __init__(self, message, is_stderr_printed):
        super().__init__(message)
        self.is_stderr_printed = is_stderr_printed