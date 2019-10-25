#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os

from .tools import logger, run_process, set_environ, execute
from .constants import WASI_CMAKE, WASI_SDK_DIR


def run(args):
    set_environ()

    if len(args) <= 1:
        print("You need to run wasiconfigure with another command (eg. `wasiconfigure ./configure`)")
        exit(1)

    return_code = run_process(args[1:], check=False)
    return return_code


if __name__ == '__main__':
    execute(run)
