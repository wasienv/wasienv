#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os

from .tools import logger, run_process, set_environ, wrap_run
from .constants import WASI_CMAKE, WASI_SDK_DIR


@wrap_run
def run(args):
    # If using cmake, we point to the toolchain file directly
    set_environ()

    if len(args) <= 1:
        print("You need to run wasimake with make or cmake (eg. `wasimake cmake .`)")
        exit(1)

    if args[1] == "cmake":
        os.environ["WASI_SDK_DIR"] = WASI_SDK_DIR
        proc_args = ["cmake", "-DCMAKE_TOOLCHAIN_FILE={}".format(WASI_CMAKE)]+args[2:]
        return_code = run_process(proc_args, check=False)
        return return_code.returncode

    return_code = run_process(args[1:], check=False)
    return return_code.returncode


if __name__ == '__main__':
    run()
