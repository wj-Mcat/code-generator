import os
from pytest import fixture
from code_generator.config import File, Directory
from code_generator.utils import (
    load_files, load_directories, gen_dynamic_text,
    load_config
)


@fixture
def data_dir() -> str:
    return './tests/data/'


def test_dynamic_text():
    text = '{{msg}}'
    data = {
        "msg": "hello world"
    }
    dynamic_text = gen_dynamic_text(text, data)
    assert dynamic_text == 'hello world'


def test_load_files(data_dir: str):
    files = load_files(data_dir)
    assert len(files) == 3


def test_load_directories(data_dir: str):
    dirs = load_directories(data_dir)
    assert len(dirs) == 3


def test_load_file_content(data_dir: str):
    a_py_file = os.path.join(data_dir, 'templates', 'a.jinja.py')
    file: File = File(path=a_py_file)
    assert file.content == '{{description}}'


def test_load_config(data_dir: str):
    config_file = os.path.join(data_dir, 'configs', 'simple.json')
    config_data = load_config(config_file)
    assert isinstance(config_data, dict)
    assert config_data['description'] == 'hello world'
