#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
from .tools import wrap_run
from .sdk import download_and_unpack, CURRENT_SDK, SDKAlreadyExists, set_default_sdk


@wrap_run
def run(args):
    if len(args) <= 1:
        print("WASIc command line tool")
        return
    if args[1] == "install-sdk":
        sdk_version = args[2]
        try:
            download_and_unpack(sdk_version)
        except SDKAlreadyExists, e:
            print(e)
    elif args[1] == "default-sdk":
        if len(args) == 3:
            sdk_version = args[2]
            set_default_sdk(sdk_version)
        else:
            print(CURRENT_SDK)


if __name__ == '__main__':
    run()
