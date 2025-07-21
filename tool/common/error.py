class Error(Exception):
    def add_prefix(self, prefix):
        super().__init__(f"{prefix}\n{self}")
        return self

class LogicError(Exception):
    pass

class SubprocessError(Exception):
    pass
