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
    version='0.2.1',
    packages=['wasienv'],
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    install_requires=[
        "requests",
    ],
    entry_points={'console_scripts': [
        'wasiar = wasienv.wasiar:run',
        'wasienv = wasienv.wasienv:run',
        'wasicc = wasienv.wasicc:run',
        'wasic++ = wasienv.wasicc:run',
        'wasiconfigure = wasienv.wasiconfigure:run',
        'wasild = wasienv.wasild:run',
        'wasimake = wasienv.wasimake:run',
        'wasirun = wasienv.wasirun:run',
        'wasinm = wasienv.wasinm:run',
        'wasiranlib = wasienv.wasiranlib:run',
    ]},
)
