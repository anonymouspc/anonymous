from common.algorithm import recursive_find
from common.config    import type, parallel
from common.run       import run
from file.module      import Module
from file.package     import Package
import os
import shutil

async def include(name, file=None, dir=None, relpath='.'):
    package = await Package(name)
    assert (file is not None) != (dir is not None)    
    if file is not None:
        if os.path.getmtime(file) != _try_getmtime(f"{package.include_dir}/{relpath}/{os.path.basename(file)}"):
            os.makedirs                           (f"{package.include_dir}/{relpath}", exist_ok=True)
            shutil.copy2(file,                     f"{package.include_dir}/{relpath}/{os.path.basename(file)}")
    if dir is not None:
        for root, _, files in os.walk(dir):
            for file in files:
                if os.path.getmtime(f"{root}/{file}") != _try_getmtime(f"{package.include_dir}/{relpath}/{os.path.relpath(root, dir)}/{file}"):
                    os.makedirs                                       (f"{package.include_dir}/{relpath}/{os.path.relpath(root, dir)}", exist_ok=True)
                    shutil.copy2   (f"{root}/{file}",                  f"{package.include_dir}/{relpath}/{os.path.relpath(root, dir)}/{file}")

async def lib(name, file):
    package = await Package(name)
    if os.path.getmtime(file) != _try_getmtime(f"{package.lib_dir}/{os.path.basename(file)}"):
        os.makedirs                           (f"{package.lib_dir}", exist_ok=True)
        shutil.copy2   (file,                  f"{package.lib_dir}/{os.path.basename(file)}")

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
    package = await Package(name)
    if not package.is_cached:
        try:
            os.makedirs(package.build_dir, exist_ok=True)
            await run(f"cmake -S {dir} "
                      f"      -B {package.build_dir} "
                      f'      -DCMAKE_PREFIX_PATH="{';'.join(await recursive_find(node=await Module(name), func=_module_to_install_dir, root=True))}" '
                      f"      -DCMAKE_INSTALL_PREFIX={package.install_dir} "
                      f"      -DCMAKE_BUILD_TYPE={type} "
                      f"{' '.join(args)}",
                      on_start=_print_progress(name))
        except:
            shutil.rmtree(package.build_dir)
            raise
    await run(f"cmake --build   ./bin/{type}/package/{name}/build -j {1 if package.is_cached else parallel}", 
              print_stderr=False, 
              parallel    =1 if package.is_cached else parallel, 
              on_start    =_print_progress(name))
    await run(f"cmake --install ./bin/{type}/package/{name}/build -j {1 if package.is_cached else parallel}",
              print_stderr=False, 
              parallel    =1 if package.is_cached else parallel, 
              on_start    =_print_progress(name))

async def autogen(name, file, args=[]):
    package = await Package(name)
    if not package.is_cached:
        await run(f"./{file} {' '.join(args)}",
                  on_start=_print_progress(name))

async def configure(name, file, args=[]):
    package = await Package(name)
    if not package.is_cached:
        try:
            os.makedirs(package.build_dir, exist_ok=True)
            await run(f"{os.path.abspath(file)} --prefix={os.path.abspath(package.install_dir)} {' '.join(args)}",
                      cwd     =package.build_dir,
                      on_start=_print_progress(name))
        except:
            shutil.rmtree(os.path.abspath(package.build_dir))
            raise

async def make(name, dir, args=[]):
    package = await Package(name)
    await run(f"make         -j {1 if package.is_cached else parallel} {' '.join(args)}", cwd=package.build_dir, print_stderr=False, parallel=1 if package.is_cached else parallel)
    await run(f"make install -j {1 if package.is_cached else parallel}",                  cwd=package.build_dir, print_stderr=False, parallel=1 if package.is_cached else parallel)

def _try_getmtime(path):
    try:
        return os.path.getmtime(path)
    except FileNotFoundError:
        return 0

async def _module_to_install_dir(module):
    return (await Package(module.name)).install_dir if await Package.exist(module.name) else None

printed_packages = []
async def _print_progress(name):
    if not (await Package(name)).is_cached and name not in printed_packages:
        Package.current += 1
        print(f"build package [{Package.current}/{Package.total}]: {name}")