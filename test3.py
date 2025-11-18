import test1

print(test1.define_macros)
import importlib
importlib.machinery.SourceFileLoader(
            fullname="test2",
            path="test2.py"
        ).load_module()
print(test1.define_macros)