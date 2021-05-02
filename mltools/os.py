import os
import shutil
from pathlib import Path


def get_or_create_dir(path_or_str):
    path = Path(path_or_str)
    if not path.exists():
        path.mkdir(parents=True)
    return path


def is_empty_dir(path_or_str):
    path = Path(path_or_str)
    return not bool(list(path.rglob("*")))


def copy_file(src_path_or_str, dst_path_or_str):
    src_path = Path(src_path_or_str)
    dst_path = Path(dst_path_or_str)
    shutil.copy(src_path, dst_path)


def remove_file(path_or_str):
    path = Path(path_or_str)
    os.remove(path)


def copy_dir(src_path_or_str, dst_path_or_str):
    src_path = Path(src_path_or_str)
    dst_path = Path(dst_path_or_str)
    shutil.copytree(src_path, dst_path)


def remove_dir(path_or_str):
    path = Path(path_or_str)
    shutil.rmtree(path)


def get_filesize(path_or_str):
    path = Path(path_or_str)
    return os.path.getsize(path)