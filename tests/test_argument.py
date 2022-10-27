import sys
from code_generator.config import Arguments


def test_render_argument():
    sys.argv = [
        '.',
        '--config=./configs'
    ]
    arguments: Arguments = Arguments().parse_args(known_only=True)
    assert arguments.config == './configs'

