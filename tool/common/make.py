from common.algorithm  import recursive_find
from common.config     import argv
from common.filesystem import exist_dir, create_dir, copy_file, copy_dir, remove_file, remove_dir, iterate_dir, absolute_path, base_path
from common.run        import run
from file.module       import Module
from file.package      import Package
import asyncio
import os
import re

async def include(name, file=None, dir=None, relpath='.'):
    package = await Package(name)
    try:
        if file is not None:
            await copy_file(file, f"{package.include_dir}/{relpath}/{base_path(file)}")
        if dir is not None:
            await copy_dir (dir,  f"{package.include_dir}/{relpath}")
    except:
        await remove_dir(package.install_dir)
        raise

async def lib(name, file):
    package = await Package(name)
    try:
        await copy_file(file, f"{package.lib_dir}/{base_path(file)}")
    except:
        await remove_dir(package.install_dir)
        raise

async def module(name, file, replace={}):
    package = await Package(name)
    try:
        with open(file, 'r') as reader:
            content = reader.read()
            content = content.replace("module;", "module;\n#undef in\n#undef self")
            for old, new in replace.items():
                content = content.replace(old, new)
        with open(package.module_file, 'w') as writer:
            writer.write(content)
    except:
        await remove_file(package.module_file)
        raise

async def format(name, relpath='.'):
    package = await Package(name)
    try:
        await asyncio.gather(*[_module_format(file) async for file in iterate_dir(f"{package.include_dir}/{relpath}", recursive=True, file_only=True)])
    except:
        await remove_dir(package.install_dir)
        raise

async def cmake(name, dir, args=[]):
    package = await Package(name)
    try:
        if not await exist_dir(package.build_dir):
            env=os.environ.copy()
            env["CXX"] = argv.compiler
            await run(
                command=[
                    "cmake",
                    "-S", dir,
                    "-B", package.build_dir,
                    f"-DCMAKE_PREFIX_PATH={';'.join(await recursive_find(node=await Module(name), func=_module_to_install_dir, root=True))}",
                    f"-DCMAKE_INSTALL_PREFIX={package.install_dir}",
                    f"-DCMAKE_INSTALL_LIBDIR=lib",
                    f"-DCMAKE_BUILD_TYPE={argv.type}",
                    *args
                ],
                env=env
            )
    except:
        await remove_dir(package.build_dir)
        raise
    try:
        await run(
            command=[
                "cmake",
                "--build", package.build_dir,
                "-j",      str(argv.parallel)
            ], 
            print_stderr=False, 
            parallel=argv.parallel
        )
    except:
        raise
    try:
        await run(
            command=[
                "cmake",
                "--install", package.build_dir,
                "-j",        str(argv.parallel)
            ],
            print_stderr=False, 
            parallel=argv.parallel
        )
    except:
        await remove_dir(package.install_dir)
        raise

async def autogen(name, file, args=[]):
    package = await Package(name)
    try:
        if not await exist_dir(package.build_dir):
            await run(
                command=[
                    absolute_path(file),
                    *args
                ]
            )
    except:
        raise

async def configure(name, file, args=[]):
    package = await Package(name)
    try:
        if not await exist_dir(package.build_dir):
            env=os.environ.copy()
            env["CXX"] = argv.compiler
            await create_dir(package.build_dir)
            await run(
                command=[
                    absolute_path(file),
                    f"--prefix={absolute_path(package.install_dir)}",
                    f"--libdir={absolute_path(package.install_dir)}/lib",
                    *args
                ],
                cwd=package.build_dir,
                env=env
            )

    except:
        await remove_dir(package.build_dir)
        raise

async def make(name, dir, args=[]):
    package = await Package(name)
    try:
        await run(
            command=[
                "make",
                "-j", str(argv.parallel),
                *args
            ],
            cwd=package.build_dir,
            print_stderr=False,
            parallel=argv.parallel
        )
    except:
        raise
    try:
        await run(
            command=[
                "make",
                "install",
                "-j", str(argv.parallel)
            ],
            cwd=package.build_dir, 
            print_stderr=False, 
            parallel=argv.parallel
        )
    except:
        await remove_dir(package.install_dir)
        raise



async def _module_format(file):
    try:
        await run(
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

async def _module_to_install_dir(module):
    return (await Package(module.name)).install_dir if await Package.exist(module.name) else None