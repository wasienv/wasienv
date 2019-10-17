#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from .tools import logger, run_process, wrap_run, check_program
from .constants import AR


@wrap_run
def run(args):
    check_program(AR)
    proc_args = [AR]+args[1:]
    return_code = run_process(proc_args, check=False)
    return return_code


if __name__ == '__main__':
    run()
