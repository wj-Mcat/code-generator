from code_generator.cli import main
import sys

sys.argv = [
    '',
    '--config=./config/',
    '--templates=./templates/vue-templates',
    '--plugins=./plugins',
    '--output_dir=./results',
    "--output_sub_name=entity_type"
]


main()
