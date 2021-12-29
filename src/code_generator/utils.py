"""
Utils methods
"""
import os
import json
from typing import List, Union
from jinja2 import Template
from code_generator.config import File, Directory


def load_files_or_directories(base_dir: str) -> List[Union[File, Directory]]:
    """
    load Files or Directories with recursion-mode
    Args:
        base_dir: the base directory

    Returns: List of File/Directory object
    """
    files_or_directories: List[Union[File, Directory]] = []

    if not os.path.exists(base_dir):
        return []

    file_or_dirs = os.listdir(base_dir)

    # 1. find all files/directories in the current dir
    for file_or_dir in file_or_dirs:

        path = os.path.join(base_dir, file_or_dir)
        # 2. if there is dir, find with recursion mode
        if os.path.isdir(path):
            directory = Directory(path)
            files_or_directories.append(directory)

            files_or_directories.extend(
                load_files_or_directories(path)
            )
        else:
            file = File(path)
            files_or_directories.append(file)

    return files_or_directories


def load_files(base_dir: str) -> List[File]:
    files_or_directories = load_files_or_directories(base_dir)
    files: List[File] = [item for item in files_or_directories if isinstance(item, File)]
    return files


def load_directories(base_dir: str) -> List[Directory]:
    files_or_directories = load_files_or_directories(base_dir)
    directories: List[Directory] = [item for item in files_or_directories if isinstance(item, Directory)]
    return directories


def gen_dynamic_text(text: str, data: dict) -> str:
    """
    generate dynamic text based on data
    Args:
        text: the source of text
        data: the dynamic data

    Returns: after rendering dynamic data of text

    """
    return Template(text).render(data)


def load_config(file: str):
    """
    load data from configuration file
    Args:
        file: the path of configuration file

    Returns:

    """
    if not os.path.exists(file):
        raise FileNotFoundError(f'file<{file}> not found')
    with open(file, 'r', encoding='utf-8') as file_handler:
        data = json.load(file_handler)
    return data


def get_file_name(file: str):
    if not os.path.isfile(file):
        raise FileExistsError(f'<{file}> is not the file ...')

    _, file_type = os.path.splitext(file)
    file_full_name = os.path.basename(file)
    file_name = file_full_name.replace(file_type, '')
    return file_name
