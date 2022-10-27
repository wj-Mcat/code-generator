"""tests code"""
import sys
import pytest
from code_generator.config import Arguments


@pytest.fixture
def simple_argument():
    sys.argv = [
        '',
        '--config=./tests/data/configs/simple.json',
        '--templates=./tests/data/templates/'
    ]


def test_loader():
    """tests template loader"""
