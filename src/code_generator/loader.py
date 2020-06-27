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
from typing import Dict, Optional
from abc import ABCMeta

from jinja2 import Template
from jinja2.runtime import Macro

from .config import get_logger

# pylint: disable=invalid-name
log = get_logger()


# pylint: disable=too-few-public-methods
class Loader(metaclass=ABCMeta):
    """load the plugins from local or default path"""
    def __init__(self, file_or_dir: str):
        """
        init the plugin files path, not load the file content,
        lazy load plugins
        """
        log.info('load file/dir <{%s}>', file_or_dir)
        self.files: Dict[str, str] = {}
        log.info('load the files from : %s', file_or_dir)
        if not os.path.exists(file_or_dir):
            log.warning('plugin file/dir doesn"t exist, there are '
                        'no plugins to load')
        self.file_or_dir = file_or_dir

    def _load_files(self):
        """load the plugins from file or dir"""
        if os.path.isdir(self.file_or_dir):
            files = os.listdir(self.file_or_dir)

            for file in files:
                file_path = os.path.join(self.file_or_dir, file)

                with open(file_path, 'r+', encoding='utf-8') as f:
                    code = f.read()
                    file_name = file

                    if '.' in file_name:
                        file_name = file_name[:file_name.rindex('.')]

                    if file_name in self.files:
                        log.warning('there are the same plugin file name : %s'
                                    , file_name)

                        # add format for file_name
                        if '.' in file_name:
                            r_index = file_name.rindex('.')
                            file_type = file_name[r_index:]
                            file_name = file_name[:r_index] + '%s' + file_type
                        else:
                            file_name = file_name + '%s'

                        file_name = file_name % '-more'

                    self.files[file_name] = code


# pylint: disable=too-few-public-methods
class TemplateLoader(Loader):
    """template loader"""
    def __init__(self, file_or_dir: str = 'templates'):
        super(TemplateLoader, self).__init__(file_or_dir)

    def load_templates(self, plugins: Optional[str] = None
                       ) -> Dict[str, Template]:
        """load template"""
        self._load_files()
        templates: Dict[str, Template] = {}
        for key, template in self.files.items():
            if plugins is not None:
                template = '{plugin}\n{template}'.format(
                    plugin=plugins, template=template
                )
            log.info(template)
            templates[key] = Template(template)
        return templates


class PluginLoader(Loader):
    """plugin loader"""
    def __init__(self, file_or_dir: str = 'templates'):
        super(PluginLoader, self).__init__(file_or_dir)

    def _load_plugins(self) -> Dict[str, str]:
        """load plugins to dict"""
        self._load_files()
        return self.files

    def load_to_file(self) -> str:
        """load plugins content to a single file content, so we can compile it
        and add it to all template"""
        files = self._load_plugins()
        return '\n'.join(files.values())

    def load_plugin_descriptions(self) -> Dict[str, str]:
        """we can set plugin with different description, so that we can use it
        to select different plugins to different field"""
        descriptions: Dict[str, str] = {}
        plugins = self._load_plugins()

        for _, plugin in plugins.items():
            module = Template(plugin).module
            attrs = dir(module)
            macros = [(attr, getattr(module, attr)) for attr in attrs
                      if isinstance(getattr(module, attr), Macro)]
            # first we only load the name of plugin
            # TODO -> we can refactor it later
            for macro_name, _ in macros:
                if macro_name not in descriptions:
                    descriptions[macro_name] = macro_name

        return descriptions

    def load_to_module(self):
        """
        load plugins to the instance of module type
        :return:
        """
        plugin_content = self.load_to_file()
        module = Template(plugin_content).module
        return module
