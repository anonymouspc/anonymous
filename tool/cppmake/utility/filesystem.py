from cppmake.basic.config import config
import functools
import os
import shutil

@functools.lru_cache
def absolute_path(path):
    return os.path.abspath(path)

@functools.lru_cache
def relative_path(path, start):
    return os.path.relpath(path, start)

@functools.lru_cache
def parent_path(path):
    return os.path.dirname(path)

@functools.lru_cache
def base_path(path):
    return os.path.basename(path)


@functools.lru_cache
def exist_file(file):
    return os.path.isfile(file)

@functools.lru_cache
def exist_dir(dir):
    return os.path.isdir(dir)


def create_file(file):
    if not exist_file(file) and config.verbose:
        print(f">>> touch {file}")
    open(file, 'w')
    exist_file.cache_clear()
    
def create_dir(dir):
    if not exist_dir(dir) and config.verbose:
        print(f">>> mkdir -p {dir}")
    os.makedirs(dir, exist_ok=True)
    exist_dir.cache_clear()


def copy_file(file, dest):
    if config.verbose:
        print(f">>> cp {file} {dest}")
    create_dir(parent_path(dest))
    shutil.copyfile(file, dest)
    exist_file.cache_clear()

def copy_dir(dir, dest):
    if config.verbose:
        print(f">>> cp -r {dir} {dest}")
    create_dir(parent_path(dest))
    shutil.copytree(dir, dest, dirs_exist_ok=True)
    exist_dir.cache_clear()


def remove_file(file):
    if exist_file(file) and config.verbose:
        print(f">>> rm {file}")
    try:
        os.remove(file)
        exist_file.cache_clear()
    except FileNotFoundError:
        pass

def remove_dir(dir):
    if exist_dir(dir) and config.verbose:
        print(f">>> rm -r {dir}")
    try:
        shutil.rmtree(dir)
        exist_dir.cache_clear()
    except FileNotFoundError:
        pass


@functools.lru_cache
def modified_time_of_file(file):
    return os.path.getmtime(file)


def iterate_dir(dir, recursive=False, file_only=False, dir_only=False):
    if not recursive:
        for item in os.listdir(dir):
            if not file_only:
                if exist_dir(f"{dir}/{item}"):
                    yield    f"{dir}/{item}"
            if not dir_only:
                if exist_file(f"{dir}/{item}"):
                    yield     f"{dir}/{item}"
    else:
        for root, dirs, files in os.walk(dir):
            if not file_only:
                for dir in dirs:
                    yield f"{root}/{dir}"
            if not dir_only:
                for file in files:
                    yield f"{root}/{file}"