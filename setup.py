# -*- coding: utf-8 -*-

from setuptools import setup
import os
import codecs


CURRENT_DIR = os.path.dirname(__file__)


def get_long_description():
    readme_md = os.path.join(CURRENT_DIR, "README.md")
    with open(readme_md) as ld_file:
        return ld_file.read()


setup(
    name='wasienv',
    description="wasienv is a C/C++ Compiler toolchain for WASI",
    # long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="webassembly wasi wasienv wasmer",
    author="Syrus Akbary",
    author_email="syrus@wasmer.io",
    url="https://github.com/wasienv-core/wasienv",
    version='0.4.0',
    packages=['wasienv'],
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    install_requires=[
        "requests",
    ],
    entry_points={'console_scripts': [
        'wasiar = wasienv.commands:wasiar',
        'wasienv = wasienv.commands:wasienv',
        'wasicc = wasienv.commands:wasicc',
        'wasic++ = wasienv.commands:wasicc',
        'wasmcc = wasienv.commands:wasmcc',
        'wasmc++ = wasienv.commands:wasmcc',
        'wasiconfigure = wasienv.commands:wasiconfigure',
        'wasild = wasienv.commands:wasild',
        'wasimake = wasienv.commands:wasimake',
        'wasirun = wasienv.commands:wasirun',
        'wasinm = wasienv.commands:wasinm',
        'wasiranlib = wasienv.commands:wasiranlib',
    ]},
)
