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
import uuid
from typing import Optional

from .config import get_logger
from .loader import TemplateLoader, PluginLoader

# pylint: disable=invalid-name
log = get_logger()
# pylint: disable=invalid-name
args_config: dict = {}


def run_server():
    """we can run a simple http server to display the code-generator"""
    from .server import run_light_server
    run_light_server()


def _save_to_file(template_dir: str, file_name: str, content: str):
    """save template result to the file"""
    if not os.path.exists(template_dir):
        os.mkdir(template_dir)
    path = os.path.join(template_dir, file_name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def _read_to_json(file: str) -> dict:
    """
    read json file to json data
    """
    file_path = os.path.join(os.getcwd(), file)
    print(file_path)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'file <{file}> not found')
    with open(file_path, 'r+', encoding='utf-8') as f:
        return json.load(f)

def render_from_server(config):
    """
    save the config to local json_file
    """
    if not os.path.exists('./config'):
        os.mkdir('./config')
    file_name = os.path.join('./config', f'config-{uuid.uuid4()}.json')
    with open(file_name, 'w+', encoding='utf-8') as f:
        if isinstance(config, dict):
            config = json.dumps(config)
        assert isinstance(config, str)
        f.write(config)
    render_by_config({
        'config': file_name,
        'templates': 'templates',
        'plugins': 'plugins'
    })


def render_by_config(params: Optional[dict] = None):
    """render the template with config file mode"""
    # pylint: disable=global-statement
    if params:
        args = params
    else:
        global args_config
        args = args_config.update(params)
        assert args is not None

    config = _read_to_json(args['config'])
    plugins = PluginLoader(args['plugins']).load_to_file()
    templates = TemplateLoader(args['templates']).load_templates(plugins)
    for name, template in templates.items():
        result = template.render(**config)
        dir_name = os.path.basename(args['templates']) + '_result'
        _save_to_file(dir_name, name, result)


def main():
    """main entry of the code-generator"""
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(help='sub command')
    serve_parser = subparsers.add_parser(name='serve')
    serve_parser.set_defaults(func=run_server)

    config_parser = subparsers.add_parser(name='render')
    config_parser.add_argument('--config', type=str, default='./config.json')
    config_parser.add_argument('--templates', type=str, default='./templates')
    config_parser.add_argument('--plugins', type=str, default='./plugins')
    config_parser.set_defaults(func=render_by_config)

    local_args = parser.parse_args()
    global args_config
    args_config.update(local_args.__dict__)
    local_args.func(args_config)


if __name__ == '__main__':
    main()
