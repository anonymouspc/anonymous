class LogicError(Exception):
    def __init__(self, message):
        super().__init__(f"error: {message}")

    def add_prefix(self, prefix):
        new_error = LogicError("")
        new_error._set_message(f"{prefix}\n{self}")
        return new_error
    
    ##### private #####

    def _set_message(self, message):
        super().__init__(message)