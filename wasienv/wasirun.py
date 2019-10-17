#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys

from .tools import logger, run_process, wrap_run


@wrap_run
def run(args):
    if len(args) < 2:
        # It should be wasirun x.wasm
        raise Exception("You need to provide a WebAssembly file")
    filename = args[1]
    proc_args = ["wasmer", "run", "--dir=.", "--enable-all", filename, "--"] + args[2:]
    return_code = run_process(proc_args, check=False)
    return return_code.returncode


if __name__ == '__main__':
    run()
