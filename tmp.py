import re
import os

for root, _, files in os.walk("./module/anonymous"):
    for file in files:
        cpp = f"{root}/{file}"
        content = open(cpp, 'r').read()
        module_name = re.findall(r'(?<=export module) ')