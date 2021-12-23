"""
generator module which handle the main logit
"""
from __future__ import annotations
import os
from typing import List, Union
from jinja2 import Template
from code_generator.config import File, Directory, Arguments
from code_generator.utils import gen_dynamic_text, load_files, load_files_or_directories, load_config


class BaseGenerator:
    def run(self, output_dir: str):
        raise NotImplementedError

    @staticmethod
    def from_template(
            file_or_dir: Union[File, Directory],
            data: dict,
            plugin_content: str = ''
    ) -> Union[FileGenerator, DirectoryGenderator]:
        if isinstance(file_or_dir, File):
            return FileGenerator(file_or_dir, data, plugin_content)
        return DirectoryGenderator(file_or_dir, data)


class FileGenerator(BaseGenerator):
    """
    render file
    """

    def run(self, output_dir: str):
        # 1. create the base file dir
        final_output_dir = os.path.join(output_dir, self.file.file_dir)
        os.makedirs(final_output_dir, exist_ok=True)
        dynamic_file_name = gen_dynamic_text(self.file.file_name, data=self.data)

        with open(os.path.join(final_output_dir, dynamic_file_name), 'w+', encoding='utf-8') as file:
            file.write(self.output_content)

    def __init__(self, file: File, data: dict, plugin_contents: str):
        self.file: File = file
        self.data = data
        self.contents = f'{file}\n{plugin_contents}'

    @property
    def output_content(self) -> str:
        content = Template(self.contents).render(self.data)
        return content


class DirectoryGenderator(BaseGenerator):
    """
    render
    """

    def run(self, output_dir: str):
        directory_path = os.path.join(output_dir, self.path)
        os.makedirs(directory_path, exist_ok=True)

    def __init__(self, directory: Directory, data: dict):
        self.path = directory.path
        self.data = data


def generate(args: Arguments):
    # 1. load plugins & template & config
    plugin_files: List[File] = load_files(args.plugins)
    plugin_content = '\n'.join([plugin_file.content for plugin_file in plugin_files])

    templates: List[Union[File, Directory]] = load_files_or_directories(args.templates)
    config_file: str = getattr(args, 'config', '')
    config_data = load_config(config_file)

    # 2. generate by templates
    for template in templates:
        generator = BaseGenerator.from_template(template, config_data, plugin_content)
        generator.run(args.output_dir)
