from cppmake.basic.main        import on_terminate, rethrow_exception, current_exception
from cppmake.utility.decorator import member
import sys

class ConfigError(Exception):
    def __init__     (self): ...
    def __terminate__():     ...



@member(ConfigError)
def __init__(self, message):
    self.args = [message]
    on_terminate(ConfigError.__terminate__)

@member(ConfigError)
def __terminate__():
    try:
        rethrow_exception(current_exception())
    except ConfigError as error:
        print(f"fatal error: {error}", file=sys.stderr)
