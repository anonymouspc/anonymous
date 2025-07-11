from common.error      import BuildError
from common.executable import Executable
from common.module     import Module
from common.object     import Object
from common.package    import Package
from common.source     import Source
import os
import sys

if __name__ == "__main__":
    open(".log", 'w')

    try:
        for root, _, files in os.walk("./test"):
            for file in files:
                Executable(f"{root.replace('/', '.').lstrip('.')}.{file.removesuffix(".cpp")}")
        for package in Package.pool.values():
            package.build()
        for module in Module.pool.values():
            module.compile()
        for source in Source.pool.values():
            source.compile()
        for object in Object.pool.values():
            object.link()
        for executable in Executable.pool.values():
            executable.run()
                
    except BuildError as e:
        print(e, end="", file=sys.stderr)
        print(e, end="", file=open(".log", 'a'))
        exit(-1)

    except KeyboardInterrupt as e:
        exit(-1)
