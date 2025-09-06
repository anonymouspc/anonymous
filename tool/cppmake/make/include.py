from cppmake.target.module      import Module
from cppmake.target.package     import Package
from cppmake.utility.filesystem import base_path, copy_file, remove_file, copy_dir, remove_dir, iterate_dir
from cppmake.utility.process    import run_process
from cppmake.utility.scheduler  import Scheduler
import asyncio
import re

async def include(name, file=None, dir=None, relpath='.'):
    package = await Package(name)
    try:
        if file is not None:
            copy_file(file, f"{package.include_dir}/{relpath}/{base_path(file)}")
        if dir is not None:
            copy_dir (dir,  f"{package.include_dir}/{relpath}")
    except:
        remove_dir(package.install_dir)
        raise

async def lib(name, file):
    package = await Package(name)
    try:
        copy_file(file, f"{package.lib_dir}/{base_path(file)}")
    except:
        remove_dir(package.install_dir)
        raise

async def module(name, file, replace={}):
    module = await Module (name)
    try:
        with open(file, 'r') as reader:
            content = reader.read()
            content = content.replace("module;", "module;\n#undef in\n#undef self")
            for old, new in replace.items():
                content = content.replace(old, new)
        with open(module.code_file, 'w') as writer:
            writer.write(content)
    except:
        remove_file(module.code_file)
        raise

async def format(name, relpath='.'):
    package = await Package(name)
    try:
        scheduler = Scheduler()
        await asyncio.gather(*[_module_format(file, scheduler=scheduler) for file in iterate_dir(f"{package.include_dir}/{relpath}", recursive=True, file_only=True)])
    except:
        remove_dir(package.install_dir)
        raise

##### private #####

async def _module_format(file, scheduler):
    async with scheduler.schedule():
        try:
            await run_process(
                command=[
                    "clang-format", 
                    "--sort-includes=false",
                    "--style={SkipMacroDefinitionBody: true}",
                    "-i", file
                ], 
                timeout=1
            )
            with open(file, 'r') as reader:
                content = reader.read()
                content = re.sub(r'^namespace\s*{',                             "inline namespace __anon__ {", content, flags=re.MULTILINE)
                content = re.sub(r'^const\b(?=[^\(\)]*;\s*$)',                  "inline const",                content, flags=re.MULTILINE)
                content = re.sub(r'^constexpr\b(?=[^\(\)]*;\s*$)',              "inline constexpr",            content, flags=re.MULTILINE)
                content = re.sub(r'^(?=\w)(?=.*inline|.*INLINE)(.*)\bstatic\b', "\\1",                         content, flags=re.MULTILINE)
                content = re.sub(r'^(?=\w)(?!.*inline|.*INLINE)(.*)\bstatic\b', "\\1inline",                   content, flags=re.MULTILINE)
            with open(file, 'w') as writer:
                writer.write(content)
        except TimeoutError:
            pass