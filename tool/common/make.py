from common.algorithm import recursive_find
from common.config    import argv
from common.run       import run
from file.module      import Module
from file.package     import Package
import asyncio
import os
import shutil

async def include(name, file=None, dir=None, relpath='.'):
    package = await Package(name)
    try:
        await _print_progress(name=name)
        os.makedirs              (f"{package.include_dir}/{relpath}", exist_ok=True)
        if file is not None:
            shutil.copyfile(file, f"{package.include_dir}/{relpath}/{os.path.basename(file)}")
        if dir is not None:
            shutil.copytree(dir,  f"{package.include_dir}/{relpath}/", dirs_exist_ok=True)
    except:
        shutil.rmtree(package.install_dir, ignore_errors=True)
        raise


async def lib(name, file):
    package = await Package(name)
    try:
        await _print_progress(name=name)
        os.makedirs          (f"{package.lib_dir}", exist_ok=True)
        shutil.copyfile(file, f"{package.lib_dir}/{os.path.basename(file)}")
    except:
        shutil.rmtree(package.install_dir, ignore_errors=True)
        raise

async def module(name, file, replace={}):
    package = await Package(name)
    try:
        await _print_progress(name=name)
        with open(file, 'r') as reader, open(package.module_file, 'w') as writer:
            content = reader.read()
            content = content.replace("module;", "module;\n#undef in\n#undef self")
            for old, new in replace.items():
                content = content.replace(old, new)
            writer.write(content)
    except:
        os.remove(package.module_file)
        raise

async def cmake(name, dir, args=[]):
    package = await Package(name)
    try:
        if not os.path.isdir(package.build_dir):
            await run(f"cmake -S {dir} "
                      f"      -B {package.build_dir} "
                      f'      -DCMAKE_PREFIX_PATH="{';'.join(await recursive_find(node=await Module(name), func=_module_to_install_dir, root=True))}" '
                      f"      -DCMAKE_INSTALL_PREFIX={package.install_dir} "
                      f"      -DCMAKE_BUILD_TYPE={argv.type} "
                      f"{' '.join(args)}",
                      on_start=_print_progress(name))
    except:
        shutil.rmtree(package.build_dir)
        raise
    try:
        await run(f"cmake --build   {package.build_dir} -j {argv.parallel}", 
                  print_stderr=False, 
                  parallel    =argv.parallel, 
                  on_start    =_print_progress(name))
    except:
        raise
    try:
        await run(f"cmake --install {package.build_dir} -j {argv.parallel}",
                  print_stderr=False, 
                  parallel    =argv.parallel, 
                  on_start    =_print_progress(name))
    except:
        shutil.rmtree(package.install_dir)
        raise

async def autogen(name, file, args=[]):
    package = await Package(name)
    try:
        if not os.path.isdir(package.build_dir):
            await run(f"{os.path.abspath(file)} {' '.join(args)}",
                      on_start=_print_progress(name))
    except:
        raise

async def configure(name, file, args=[]):
    package = await Package(name)
    try:
        if not os.path.isdir(package.build_dir):
            os.makedirs(package.build_dir, exist_ok=True)
            await run(f"{os.path.abspath(file)} --prefix={os.path.abspath(package.install_dir)} {' '.join(args)}",
                      cwd     =package.build_dir,
                      on_start=_print_progress(name))
    except:
        shutil.rmtree(package.build_dir, ignore_errors=True)
        raise

async def make(name, dir, args=[]):
    package = await Package(name)
    try:
        await run(f"make -j {argv.parallel} {' '.join(args)}", 
                  cwd         =package.build_dir,
                  print_stderr=False,
                  parallel    =argv.parallel,
                  on_start    =_print_progress(name))
    except:
        raise
    try:
        await run(f"make install -j {argv.parallel}",                  
                  cwd         =package.build_dir, 
                  print_stderr=False, 
                  parallel    =argv.parallel,
                  on_start    =_print_progress(name))
    except:
        shutil.rmtree(package.install_dir, ignore_errors=True)
        raise

async def _module_to_install_dir(module):
    return (await Package(module.name)).install_dir if await Package.exist(module.name) else None

_printed_progress = []
async def _print_progress(name):
    global _printed_progress
    if name not in _printed_progress:
        Package.current += 1
        print(f"build package [{Package.current}/{Package.total}]: {name}")
        _printed_progress += [name]