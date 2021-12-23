# Makefile for Code Generator
#
# 	GitHb: https://github.com/wj-Mcat/code-generator
#
# 	Author: Jingjing WU (吴京京) <https://github.com/wj-Mcat>

SOURCE_GLOB=$(wildcard bin/*.py src/**/*.py tests/**/*.py examples/*.py)

IGNORE_PEP=E203,E221,E241,E272,E501,F811,C0115

# help scripts to find the right place of wechaty module
export PYTHONPATH=src/

.PHONY: all
all : clean lint

.PHONY: clean
clean:
	rm -fr dist/* ./build/ ./dist/

.PHONY: lint
lint: pylint pycodestyle flake8 mypy

.PHONY: pylint
pylint:
	pylint \
		--load-plugins pylint_quotes \
		--disable=W0511,R0801,cyclic-import,C0115 \
		$(SOURCE_GLOB)

.PHONY: pycodestyle
pycodestyle:
	pycodestyle \
		--statistics \
		--count \
		--ignore="${IGNORE_PEP}" \
		$(SOURCE_GLOB)

.PHONY: flake8
flake8:
	flake8 \
		--ignore="${IGNORE_PEP}" \
		$(SOURCE_GLOB)

.PHONY: mypy
mypy:
	MYPYPATH=stubs/ mypy \
		$(SOURCE_GLOB)

.PHONY: install
install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

.PHONY: pytest
pytest:
	pytest src/ tests/

.PHONY: test-unit
test-unit: pytest

.PHONY: test
test: lint pytest

code:
	code .

.PHONY: dist
dist:
	python setup.py sdist bdist_wheel

.PHONY: publish
publish: clean dist
		PATH=~/.local/bin:${PATH} twine upload dist/*

.PHONY: local_dist
local_dist:
	pip uninstall code-generator
	make dist
	pip install dist/code_generator-0.0.3-py3-none-any.whl
