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

from setuptools import setup, find_packages

with open("./VERSION", 'r+') as f:
    VERSION = f.read()

with open('./requirements.txt', 'r+') as f:
    requirements = f.readlines()

with open('./README.md', 'r+') as f:
    long_description = f.read()
    long_description = 'full document please check the github: ' \
                       'https://www.github.com/wj-Mcat/code-generator'

setup(
    name='code-generator',
    version=VERSION,
    description="a simple code generator for all-language",
    long_description=long_description,
    keywords='code-gen,code-generator,python,code-snippet',
    author='wj-Mcat',
    author_email='1435130236@qq.com',
    license='Apache 2',
    packages=find_packages('src'),
    package_dir={
        "": "src"
    },
    include_package_data=True,
    package_data = {
        'code_generator': ['templates/vue/dist/*', 'static/*']
    },
    install_requires=requirements,
    entry_points={
      'console_scripts': [
          'code-gen=code_generator.main:main'
      ]
  }
)