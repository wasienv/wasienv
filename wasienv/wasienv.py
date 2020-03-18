#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
from .tools import execute
from .sdk import download_and_unpack, CURRENT_SDK, SDKAlreadyExists, set_default_sdk, install_swiftwasm


def run(args):
    if len(args) <= 1:
        print("wasienv command line tool")
        return
    if args[1] == "install-sdk":
        sdk_version = args[2]
        try:
            download_and_unpack(sdk_version)
        except SDKAlreadyExists as e:
            print(e)
    elif args[1] == "install-swift":
        swift_version = args[2] if len(args) > 2 else None
        install_swiftwasm(swift_version)
    elif args[1] == "default-sdk":
        if len(args) == 3:
            sdk_version = args[2]
            set_default_sdk(sdk_version)
        else:
            print(CURRENT_SDK)
    else:
        print("Command {} not found".format(args[1]))

if __name__ == '__main__':
    execute(run)
