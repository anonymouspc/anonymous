import cppmake
import re

async def std():
    if cppmake.compiler.name == "clang":
        compiler_path = await cppmake.run_process(["which", cppmake.compiler.path], return_stdout=True)
        cppm_path     = f"{cppmake.parent_path(compiler_path)}/../share/libc++/v1/std.cppm"
        module_path   = "./module/std/compiler/clang.cpp"
        with open(cppm_path, 'r') as reader:
            cppm_data = reader.readlines()
        for index in range(len(cppm_data)):
            try:
                cppm_data[index] = re.sub("module;",            "module;\n#undef in",                cppm_data[index])
                cppm_data[index] = re.sub("export module std;", "export module std:compiler.clang;", cppm_data[index])
                cppm_data[index] = open(f"{cppmake.parent_path(cppm_path)}/{re.match(r'#include "(std/.*)"', cppm_data[index])[1]}", 'r').read() + '\n'
            except TypeError:
                pass
        with open(module_path, 'w') as writer:
            writer.writelines(cppm_data)

cppmake.main(std())
                