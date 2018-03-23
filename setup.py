#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'ruamel.yaml>=0.15.35', 'requests', 'nameparser']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Stefan Verhoeven",
    author_email='s.verhoeven@esciencecenter.nl',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Create citation file formatted file from a Github/Zenodo release",
    entry_points={
        'console_scripts': [
            'doi2cff=doi2cff.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='doi2cff',
    name='doi2cff',
    packages=find_packages(include=['doi2cff']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/3D-e-Chem/doi2cff',
    version='1.0.0',
    zip_safe=False,
)
