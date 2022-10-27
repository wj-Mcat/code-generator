"""
Code Generator - https://github.com/wj-Mcat/code-generator

Authors:    Jingjing WU (吴京京) <https://github.com/wj-Mcat>

2020-now @ Copyright wj-Mcat

Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from __future__ import annotations
import os

from tap import Tap
from loguru import logger


def get_logger():
    """
    use the loguru as the default logger
    """
    return logger


class Arguments(Tap):
    output_dir: str = './output'
    templates: str = './templates'
    plugins: str = './plugins'
    config: str = './config.json'


class File:
    def __init__(self, path: str):
        if not os.path.isfile(path):
            raise IsADirectoryError(f'path<{path}> is not a file')

        self.file_name = os.path.basename(path)
        self.file_dir = os.path.dirname(path)
        self.path = path

    @property
    def type(self) -> str:
        _, file_type = os.path.splitext(self.path)
        return file_type

    @property
    def content(self):
        """
        get the content of file
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content

    def __str__(self):
        return f'File<{self.path}>'


class Directory:
    def __init__(self, path: str):
        if not os.path.isdir(path):
            raise IsADirectoryError()
        self.path = path

    def __str__(self):
        return f'Directory<{self.path}>'
