class LogicError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def add_prefix(self, prefix):
        super().__init__(f"{prefix}\n{self}")