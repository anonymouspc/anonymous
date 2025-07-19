from common.algorithm import recursive_find
from common.config    import type
from common.run       import run
from file.module      import Module
from file.package     import Package
import os
import shutil

async def include(name, file=None, dir=None, relpath='.'):
    assert (file is not None) != (dir is not None)    
    if file is not None:
        if os.path.getmtime(file) != _try_getmtime(f"./bin/{type}/package/{name}/install/include/{relpath}/{os.path.basename(file)}"):
            os.makedirs                           (f"./bin/{type}/package/{name}/install/include/{relpath}", exist_ok=True)
            shutil.copy2(file,                     f"./bin/{type}/package/{name}/install/include/{relpath}/{os.path.basename(file)}")
    if dir is not None:
        for root, _, files in os.walk(dir):
            for file in files:
                if os.path.getmtime(f"{root}/{file}") != _try_getmtime(f"./bin/{type}/package/{name}/install/include/{relpath}/{os.path.relpath(root, dir)}/{file}"):
                    os.makedirs                                       (f"./bin/{type}/package/{name}/install/include/{relpath}/{os.path.relpath(root, dir)}", exist_ok=True)
                    shutil.copy2   (f"{root}/{file}",                  f"./bin/{type}/package/{name}/install/include/{relpath}/{os.path.relpath(root, dir)}/{file}")

async def lib(name, file):
    if os.path.getmtime(file) != _try_getmtime(f"./bin/{type}/package/{name}/install/lib/{os.path.basename(file)}"):
        os.makedirs                           (f"./bin/{type}/package/{name}/install/lib", exist_ok=True)
        shutil.copy2   (file,                  f"./bin/{type}/package/{name}/install/lib/{os.path.basename(file)}")

async def module(name, file, replace={}):
    if os.path.getmtime(file) != _try_getmtime(f"./module/{name}.cpp"):
        with open(file, 'r') as reader, open(f"./module/{name}.cpp", 'w') as writer:
            content = reader.read()
            content = content.replace("module;", "module;\n#undef in\n#undef self")
            for old, new in replace.items():
                content = content.replace(old, new)
            writer.write(content)
        os.utime(f"./module/{name}.cpp", (os.path.getatime(file), os.path.getmtime(file)))

async def cmake(name, dir, args=[]):
    if not os.path.isdir(f"./bin/{type}/package/{name}/build"):
        await run(f"cmake -S ./{dir} "
                  f"      -B ./bin/{type}/package/{name}/build "
                  f'      -DCMAKE_PREFIX_PATH="{';'.join(await recursive_find(node=await Module(name), func=_module_to_install_dir, root=True))}" '
                  f"      -DCMAKE_INSTALL_PREFIX=./bin/{type}/package/{name}/install "
                  f"      -DCMAKE_BUILD_TYPE={type} "
                  f"{' '.join(args)}")
    await run(f"cmake --build   ./bin/{type}/package/{name}/build -j {os.cpu_count()}", print_stderr=False)
    await run(f"cmake --install ./bin/{type}/package/{name}/build -j {os.cpu_count()}", print_stderr=False)

async def autogen(name, file, args=[]):
    if not os.path.isdir(f"./bin/{type}/package/{name}/build"):
        await run(f"./{file} {' '.join(args)}")

async def configure(name, file, args=[]):
    if not os.path.isdir(f"./bin/{type}/package/{name}/build"):
        cwd = f"./bin/{type}/package/{name}/build"
        try:
            os.makedirs(cwd, exist_ok=True)
            await run(f"./{os.path.relpath(file, cwd)} --prefix={os.path.abspath(f"./bin/{type}/package/{name}/install")} {' '.join(args)}", cwd=cwd)
        except:
            shutil.rmtree(cwd)
            raise

async def make(name, dir, args=[]):
    cwd = f"./bin/{type}/package/{name}/build"
    await run(f"make         -j{os.cpu_count()} {' '.join(args)}", cwd=cwd, print_stderr=False)
    await run(f"make install -j{os.cpu_count()}",                  cwd=cwd, print_stderr=False)

async def nmake(name, dir, args=[]):
    cwd = f"./bin/{type}/package/{name}/build"
    await run(f"nmake         -j{os.cpu_count()} {' '.join(args)}", cwd=cwd, print_stderr=False)
    await run(f"nmake install -j{os.cpu_count()}",                  cwd=cwd, print_stderr=False)

def _try_getmtime(path):
    try:
        return os.path.getmtime(path)
    except FileNotFoundError:
        return 0

async def _module_to_install_dir(module):
    return (await Package(module.name)).install_dir if await Package.exist(module.name) else None