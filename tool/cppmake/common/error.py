from cppmake.common.logger import compile_output_logger

class LogicError(Exception):
    def __init__(self, message):
        super().__init__(f"error: {message}")

    def add_prefix(self, prefix):
        super().__init__(f"{prefix}\n{self}")
        return self

class SubprocessError(Exception):
    def __init__(self, message, is_stderr_printed):
        super().__init__(message)
        self.is_stderr_printed = is_stderr_printed
        compile_output_logger.log(message)
            

