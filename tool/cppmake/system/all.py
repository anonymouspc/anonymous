from cppmake.error.logic    import LogicError
from cppmake.system.linux   import Linux
from cppmake.system.macos   import Macos
from cppmake.system.windows import Windows

if Linux.check():
    system = Linux()
elif Macos.check():
    system = Macos()
elif Windows.check():
    system = Windows()
else:
    raise LogicError("unrecognized system")