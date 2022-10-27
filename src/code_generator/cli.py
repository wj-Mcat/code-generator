"""
command line utils
"""
from code_generator.config import Arguments, get_logger
from code_generator.generator import generate


log = get_logger()


def main():
    args = Arguments().parse_args(known_only=True)
    generate(args)
