import atexit
import sys

def _on_exit():
    pass

def _on_error(type, value, traceback):
    if type.__module__.startswith("cppmake.error"):
        value.at_exit()
        exit(-1)
    else:
        sys.__excepthook__(type, value, traceback)

atexit.register(_on_exit)
sys.excepthook = _on_error
    