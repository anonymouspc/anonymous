import sys

class ConfigError(Exception):
    def at_exit(self):
        print(f"error: {self}", file=sys.stderr)