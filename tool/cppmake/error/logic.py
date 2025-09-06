class LogicError(Exception):
    def __init__(self, message):
        super().__init__(f"error: {message}")

    def add_prefix(self, prefix):
        super().__init__(f"{prefix}\n{self}")
        return self