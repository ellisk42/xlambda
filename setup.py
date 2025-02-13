# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup
from distutils.command.build import build
from setuptools.command.install import install

from setuptools.command.develop import develop

import os
BASEPATH = os.path.dirname(os.path.abspath(__file__))

setup(name='lambdabeam',
      py_modules=['lambdabeam'],
      install_requires=[
        'absl-py',
        'matplotlib',
        'ml_collections',
        'numpy',
        'pickle5',
        'pytest',
        'seaborn',
        'tensorboard',
        'tqdm',
        'torch',
        'torch_scatter',
        'setuptools==59.5.0',
      ]
)
