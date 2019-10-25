#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os

from .tools import logger, run_process, try_to_wrap_executable, find_output_arg, execute, check_program
from .constants import CC, CXX, WASI_SYSROOT, STUBS_SYSTEM_LIB, STUBS_SYSTEM_PREAMBLE


def run(args):
    main_program = CXX if args[0].endswith("wasic++") else CC
    check_program(main_program)
    if '--version' in args:
        print('''wasienv (wasienv gcc/clang-like replacement)''')
        return 0

    if len(args) == 1 and args[0] == '-v': # -v with no inputs
        # autoconf likes to see 'GNU' in the output to enable shared object support
        print('wasienv (wasienv gcc/clang-like replacement + linker emulating GNU ld)', file=sys.stderr)
        code = run_process([main_program, '-v'], check=False).returncode
        return code

    has_sysroot = any([arg.startswith("--sysroot") for arg in args])
    has_target = any([arg.startswith("--target") for arg in args])
    
    args.append('-isystem{}'.format(STUBS_SYSTEM_LIB))
    args.append('-include{}'.format(STUBS_SYSTEM_PREAMBLE))
    args.append('-D_WASI_EMULATED_MMAN')

    if not has_sysroot:
        args.append("--sysroot={}".format(WASI_SYSROOT))

    if not has_target:
        args.append("--target=wasm32-wasi")

    proc_args = [main_program]+args[1:]
    return_code = run_process(proc_args, check=False)
    target, outargs = find_output_arg(args)
    if target:
        try_to_wrap_executable(target)
    return return_code


if __name__ == '__main__':
    execute(run)
