from common.algorithm import recursive_find
from common.config    import system, type
from common.error     import BuildError
from common.module    import Module
from common.package   import Package
from common.run       import run
import os
import shutil

def include(name, dir=None, file=None):
    if dir is not None:
        shutil.copytree(dir,  f"./bin/{type}/package/{name}/install/include", dirs_exist_ok=True)
    if file is not None:
        os.makedirs          (f"./bin/{type}/package/{name}/install/include", exist_ok=True)
        shutil.copyfile(file, f"./bin/{type}/package/{name}/install/include/{os.path.basename(file)}")
    if dir is None and file is None:
        raise BuildError("include() accepts at least 2 arguments")

def src(name, dir, src_to_include=None):
    if src_to_include is None:
        src_to_include = f"{name}/src"
    shutil.copytree(dir, f"./bin/{type}/package/{name}/install/include/{src_to_include}", dirs_exist_ok=True)

def module(name, file, replace={}):
    with open(file, 'r') as reader, open(f"./module/{name}.cpp", 'w') as writer:
        content = reader.read()
        content = content.replace("module;", "module;\n#undef in\n#undef self")
        for old, new in replace.items():
            content = content.replace(old, new)
        writer.write(content)

def cmake(name, dir, args=[]):
    run(f"cmake -S ./{dir} "
            f"      -B ./bin/{type}/package/{name}/build "
            f'      -DCMAKE_PREFIX_PATH="{';'.join(recursive_find(node=Module(name), func=lambda module: Package(module.name).install_dir if Package.exist(module.name) else None, root=True))}" '
            f"      -DCMAKE_INSTALL_PREFIX=./bin/{type}/package/{name}/install "
            f"      -DCMAKE_BUILD_TYPE={type} "
            f"{' '.join(args)}")
    run(f"cmake --build   ./bin/{type}/package/{name}/build -j {os.cpu_count()}", quiet=True)
    run(f"cmake --install ./bin/{type}/package/{name}/build -j {os.cpu_count()}")

def autogen(name, file, args=[]):
    if not Package(name).is_configured:
        run(f"./{file} {' '.join(args)}")

def configure(name, file, args=[]):
    if not Package(name).is_configured:
        cwd = f"./bin/{type}/package/{name}/build"
        try:
            os.makedirs(cwd, exist_ok=True)
            run(f"./{os.path.relpath(file, cwd)} --prefix={os.path.abspath(f"./bin/{type}/package/{name}/install")} {' '.join(args)}", cwd=cwd)
        except:
            shutil.rmtree(cwd)
            raise

def make(name, dir, args=[]):
    if system == "linux" or system == "macos":
        cwd = f"./bin/{type}/package/{name}/build"
        run(f"make         -j{os.cpu_count()} {' '.join(args)}", cwd=cwd, quiet=True)
        run(f"make install -j{os.cpu_count()}",                  cwd=cwd, quiet=True)
    else:
        raise BuildError("make is only supported on linux and macos")

def nmake(name, dir, args=[]):
    if system == "windows":
        cwd = f"./bin/{type}/package/{name}/build"
        run(f"nmake         -j{os.cpu_count()} {' '.join(args)}", cwd=cwd, quiet=True)
        run(f"nmake install -j{os.cpu_count()}",                  cwd=cwd, quiet=True)
    else:
        raise BuildError("nmake is only supported on windows")