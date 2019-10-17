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
    name='wasic',
    description="Wasic is a C/C++ Compiler toolchain for WASI",
    # long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="webassembly wasi wasic wasmer",
    author="Syrus Akbary",
    author_email="syrus@wasmer.io",
    url="https://github.com/wasic-core/wasic",
    version='0.1.6',
    packages=['wasic'],
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    entry_points={'console_scripts': [
        'wasiar = wasic.wasiar:run',
        'wasic = wasic.wasic:run',
        'wasicc = wasic.wasicc:run',
        'wasic++ = wasic.wasicc:run',
        'wasiconfigure = wasic.wasiconfigure:run',
        'wasild = wasic.wasild:run',
        'wasimake = wasic.wasimake:run',
        'wasirun = wasic.wasirun:run',
        'wasinm = wasic.wasinm:run',
        'wasiranlib = wasic.wasiranlib:run',
    ]},
)
