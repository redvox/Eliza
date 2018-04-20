#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from version import __version__
from setuptools import setup

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    dependencies = f.read().splitlines()

version = '.'.join(str(x) for x in __version__)

setup(
    name='Eliza',
    version=version,
    description='Library with common features for Python (Flask) Microservices',
    url='https://github.com/redvox/Eliza',
    download_url = 'https://github.com/redvox/Eliza/tarball/'+version,
    author='Jens Schaa',
    author_email="jens.schaa@posteo.de",
    packages=[
        'eliza',
    ],
    package_data={},
    license='Apache Software License',
    install_requires=dependencies,
    test_suite='test.test_data',
    long_description=open('README.md').read(),
    classifiers=(
        b'Development Status :: 4 - Beta',
        b'Intended Audience :: Developers',
        b'Natural Language :: English',
        b'License :: OSI Approved :: Apache Software License',
        b'Programming Language :: Python',
        b'Programming Language :: Python :: 2.7',
        b'Programming Language :: Python :: 3',
        b'Programming Language :: Python :: 3.4',
        b'Programming Language :: Python :: 3.5'
    )
)
