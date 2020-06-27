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

import json
from argparse import ArgumentParser
import os

from .config import get_logger
from .loader import TemplateLoader, PluginLoader

# pylint: disable=invalid-name
log = get_logger()
# pylint: disable=invalid-name
args: dict = {}


def run_server():
    """we can run a simple http server to display the code-generator"""


def _save_to_file(template_dir: str, file_name: str, content: str):
    """save template result to the file"""
    if not os.path.exists(template_dir):
        os.mkdir(template_dir)
    path = os.path.join(template_dir, file_name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def _read_to_json(file: str) -> dict:
    """read json file to json data"""
    file_path = os.path.join(os.getcwd(), file)
    print(file_path)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'file <{file}> not found')
    with open(file_path, 'r+', encoding='utf-8') as f:
        return json.load(f)


def render_by_config():
    """render the template with config file mode"""
    config = _read_to_json(args['config'])
    plugins = PluginLoader(args['plugins']).load_to_file()
    log.info(plugins)
    templates = TemplateLoader(args['templates']).load_templates(plugins)
    for name, template in templates.items():
        result = template.render(config)
        base_name = os.path.basename(args['templates']) + '_result'
        _save_to_file(base_name, name, result)


def main():
    """main entry of the code-generator"""
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(help='sub command')
    serve_parser = subparsers.add_parser(name='serve')
    serve_parser.add_argument('--model', default='models', type=str)
    serve_parser.add_argument('--port', default=5002, type=int)
    serve_parser.add_argument('--file', default='config.json', type=str)
    serve_parser.set_defaults(func=run_server)

    config_parser = subparsers.add_parser(name='render')
    config_parser.add_argument('--config', type=str, default='./config.json')
    config_parser.add_argument('--templates', type=str, default='./templates')
    config_parser.add_argument('--plugins', type=str, default='./plugins')
    config_parser.set_defaults(func=render_by_config)

    local_args = parser.parse_args()
    log.info(args)
    args.update(local_args.__dict__)
    local_args.func()


if __name__ == '__main__':
    main()
