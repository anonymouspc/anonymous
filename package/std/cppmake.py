from cppmakelib import *
import shutil

if type(compiler) is Clang:
    package.compile_flags += [
        "-Wno-include-angled-in-module-purview",
        "-Wno-reserved-module-identifier"
    ]
        
def build():
    include_file = f"{package.include_dir}/include"
    export_file  = f"{package.include_dir}/export"
    if type(compiler) is Gcc:
        libstdcxx_dir = f"{parent_path(shutil.which(compiler.path))}/../include/c++/{compiler.version[0]}"
        std_file      = f"{libstdcxx_dir}/bits/std.cc"
    elif type(compiler) is Clang:
        libcxx_dir = f"{run(command=[compiler.path, "--print-resource-dir"], return_stdout=True).removesuffix('\n')}/../../../share/libc++/v1"
        std_file   = f"{libcxx_dir}/std.cppm"
        copy_dir(libcxx_dir, package.include_dir)
    else:
        assert False
    try:
        create_dir(package.include_dir)
        with open(std_file, 'r') as reader:
            content = reader.read().split("export module std;")
        with open(include_file, 'w') as writer:
            writer.write(content[0].replace("module;", ""))
        with open(export_file, 'w') as writer:
            writer.write(content[1])
    except FileNotFoundError as error:
        raise LogicError(f'std module file {error.filename} not found (with compiler = {compiler.path})')
        

        