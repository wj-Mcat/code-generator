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
from argparse import ArgumentParser

from .config import get_logger
from .loader import TemplateLoader, PluginLoader


log = get_logger()
args = {}


def run_server():
    pass


def render_by_config():
    file = args['file']
    templates = TemplateLoader(file).load_templates()
    plugin_file = PluginLoader(file).load_to_file()




def main():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(help='sub command')
    serve_parser = subparsers.add_parser(name='serve')
    serve_parser.add_argument('--model', default='models', type=str)
    serve_parser.add_argument('--port', default=5002, type=int)
    serve_parser.add_argument('--file', default='config.json', type=str)
    serve_parser.set_defaults(func=run_server)

    config_parser = subparsers.add_parser(name='config')
    config_parser.add_argument('--file', default='config.json', type=str)
    config_parser.add_argument('--template', default='flask,vue', type=str)
    config_parser.set_defaults(func=render_by_config)

    local_args = parser.parse_args()
    log.info(args)
    args.update(local_args.__dict__)
    local_args.func(args)


if __name__ == '__main__':
    main()
