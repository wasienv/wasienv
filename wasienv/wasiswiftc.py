#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os

from .tools import logger, run_process, try_to_wrap_executable, find_output_arg, execute, check_program
from .constants import CC, CXX, WASI_SYSROOT, STUBS_SYSTEM_LIB, STUBS_SYSTEM_PREAMBLE
from .sdk import SWIFTENV_BIN

def run(args):
    # check_program(SWIFTENV_BIN)
    # check_program("swiftc")
    # SWIFTWASIBIN = run_process([SWIFTENV_BIN, "--shim", "swiftc", "swiftc"], get_output=True).strip()
    SWIFTWASIBIN = run_process([SWIFTENV_BIN, "which", "swiftc"], get_output=True).strip()
    TOOLCHAIN_PATH = os.path.dirname(os.path.dirname(SWIFTWASIBIN))
    
    MODULE_MAP = os.path.join(TOOLCHAIN_PATH, "lib/swift/wasi/wasm32/glibc.modulemap")
    # /Users/syrusakbary/.swiftenv/versions/wasm-DEVELOPMENT-SNAPSHOT-2020-03-08-a/usr/
    WASI_SYSROOT = os.path.join(TOOLCHAIN_PATH, "share", "wasi-sysroot")
    
    # proc_args = [SWIFTENV_BIN, "exec", "--shim", "swiftc"]+args[1:]
    # SDK_ROOT = 
    proc_args = [SWIFTWASIBIN, "-target", "wasm32-unknown-wasi", "-sdk", WASI_SYSROOT]+args[1:]
    return_code = run_process(proc_args, check=False)
    target, outargs = find_output_arg(args)
    if target:
        try_to_wrap_executable(target)
    return return_code


if __name__ == '__main__':
    execute(run)
