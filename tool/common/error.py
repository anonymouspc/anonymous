from common.logger import compile_output_logger

class Error(Exception):
    def add_prefix(self, prefix):
        return type(self)(f"{prefix}\n{self}")

class LogicError(Error):
    pass

class SubprocessError(Error):
    def __init__(self, message, is_stderr_printed):
        super().__init__(message)
        self.is_stderr_printed = is_stderr_printed
        compile_output_logger.log(message)
            

