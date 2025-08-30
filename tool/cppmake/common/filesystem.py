from cppmake.common.config import argv
import os
import shutil

async def exist_file(file):
    return os.path.isfile(file)

async def exist_dir(dir):
    return os.path.isdir(dir)

async def create_file(file):
    if argv.verbose:
        print(f"create file: {file}")
    open(file, 'w')
    
async def create_dir(dir):
    if argv.verbose:
        print(f"create dir: {dir}")
    os.makedirs(dir, exist_ok=True)

async def copy_file(file, dest):
    if argv.verbose:
        print(f"copy file: {file} -> {dest}")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copyfile(file, dest)

async def copy_dir(dir, dest):
    if argv.verbose:
        print(f"copy directory: {dir} -> {dest}")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copytree(dir, dest, dirs_exist_ok=True)

async def remove_file(file):
    if argv.verbose:
        print(f"remove file: {file}")
    os.remove(file)

async def remove_dir(dir):
    if argv.verbose:
        print(f"remove dir: {dir}")
    shutil.rmtree(dir, ignore_errors=True)

async def iterate_dir(dir, recursive=False, file_only=False, dir_only=False):
    if not recursive:
        for item in os.listdir(dir):
            if not file_only:
                if await exist_dir(f"{dir}/{item}"):
                    yield f"{dir}/{item}"
            if not dir_only:
                if await exist_file(f"{dir}/{item}"):
                    yield f"{dir}/{item}"
    else:
        for root, dirs, files in os.walk(dir):
            if not file_only:
                for dir in dirs:
                    yield f"{root}/{dir}"
            if not dir_only:
                for file in files:
                    yield f"{root}/{file}"

async def getmtime_file(file):
    return os.path.getmtime(file)

def absolute_path(path):
    return os.path.abspath(path)

def relative_path(path, start):
    return os.path.relpath(path, start)

def parent_path(path):
    return os.path.dirname(path)

def base_path(path):
    return os.path.basename(path)