import os
import sys
import platform
try:
    # Python 3
    from io import BytesIO as StringIO
except ImportError:
    from StringIO import StringIO

import requests
import tarfile

from .tools import logger

# Where the python packages live
PACKAGES_DIR    = os.path.dirname(os.path.dirname(__file__))

# Where the wasienv storage lives
WASI_STORAGE_DIR    = os.path.join(PACKAGES_DIR, "wasienv-storage")
WASI_SDKS_DIR = os.path.join(WASI_STORAGE_DIR, "sdks")

CURRENT_SDK = "8"

SDKS = {
    "5": {
        "download_urls": {
            "darwin": 'https://github.com/CraneStation/wasi-sdk/releases/download/wasi-sdk-5/wasi-sdk-5.0-macos.tar.gz',
            "linux": 'https://github.com/CraneStation/wasi-sdk/releases/download/wasi-sdk-5/wasi-sdk-5.0-linux.tar.gz',
        },
        "sysroot": "wasi-sdk-5.0/opt/wasi-sdk"
    },
    "6": {
        "download_urls": {
            "darwin": 'https://github.com/CraneStation/wasi-sdk/releases/download/wasi-sdk-6/wasi-sdk-6.0-macos.tar.gz',
            "linux": 'https://github.com/CraneStation/wasi-sdk/releases/download/wasi-sdk-6/wasi-sdk-6.0-linux.tar.gz',
        },
        "sysroot": "wasi-sdk-6.0/opt/wasi-sdk"
    },
    "7": {
        "download_urls": {
            "darwin": 'https://github.com/CraneStation/wasi-sdk/releases/download/wasi-sdk-7/wasi-sdk-7.0-macos.tar.gz',
            "linux": 'https://github.com/CraneStation/wasi-sdk/releases/download/wasi-sdk-7/wasi-sdk-7.0-linux.tar.gz',
        },
        "sysroot": "wasi-sdk-7.0/opt/wasi-sdk"
    },
    "8": {
        "download_urls": {
            "darwin": 'https://github.com/CraneStation/wasi-sdk/releases/download/wasi-sdk-8/wasi-sdk-8.0-macos.tar.gz',
            "linux": 'https://github.com/CraneStation/wasi-sdk/releases/download/wasi-sdk-8/wasi-sdk-8.0-linux.tar.gz',
        },
        "sysroot": "wasi-sdk-8.0/opt/wasi-sdk"
    },
}

SDK_TAGS = {
    "latest": "8",
    "unstable": "8"
}


class SDKException(Exception):
    pass


class SDKAlreadyExists(SDKException):
    pass


class SDKNotInstalled(SDKException):
    pass


def get_sdk_dir(sdk_name):
    return os.path.join(WASI_SDKS_DIR, sdk_name)


def unalias_name(sdk_name):
    if sdk_name in SDK_TAGS:
        sdk_name = SDK_TAGS[sdk_name]
    return sdk_name


def get_sdk(sdk_name):
    sdk = SDKS.get(sdk_name)
    if not sdk:
        raise SDKException("The SDK {} doesn't exist".format(sdk_name))
    return sdk


def is_sdk_installed(sdk_name):
    sdk_name = unalias_name(sdk_name)
    sdk = get_sdk(sdk_name)
    sdk_dir = get_sdk_dir(sdk_name)
    return os.path.exists(sdk_dir) and os.path.isdir(sdk_dir) and bool(os.listdir(sdk_dir))


def download_and_unpack(sdk_name):
    sdk_name = unalias_name(sdk_name)
    sdk = get_sdk(sdk_name)
    download_urls = sdk.get("download_urls", {})
    if is_sdk_installed(sdk_name):
        raise SDKAlreadyExists("The SDK {} is already installed".format(sdk_name))
    system = platform.system()
    download_url = download_urls.get(system.lower(), None)
    if not download_url:
        raise SDKException("The SDK {} doesn't have an installable for {}".format(sdk_name, system))

    sdk_dir = get_sdk_dir(sdk_name)
    logger.info("Downloading WASI SDK to: {} from: {}".format(sdk_dir, download_url))
    response = requests.get(download_url)
    logger.info("SDK Downloaded, uncompressing")
    tf = tarfile.open(fileobj=StringIO(response.content))
    os.makedirs(sdk_dir)
    tf.extractall(sdk_dir)
    # Assert the sysroot dir was created
    sysroot = get_sdk_sysroot(sdk, sdk_name)
    if not os.path.isdir(sysroot):
        raise SDKException("The SDK expected sysroot doesn't exist: {}".format(sysroot))
    logger.info("SDK installed successfully")


def get_sdk_sysroot(sdk, sdk_name):
    if not sdk:
        raise Exception("SDK {} not found".format(sdk_name))
    if "sysroot" not in sdk:
        raise Exception("SDK {} doesn't have a sysroot defined".format(sdk_name))
    return os.path.join(get_sdk_dir(sdk_name), sdk["sysroot"])


def set_default_sdk(sdk_name):
    sdk_name = unalias_name(sdk_name)
    sdk = get_sdk(sdk_name)
    if not is_sdk_installed(sdk_name):
        raise SDKNotInstalled("The SDK {} is not installed".format(sdk_name))


WASI_SDK = get_sdk(CURRENT_SDK)
WASI_SDK_DIR = get_sdk_sysroot(WASI_SDK, CURRENT_SDK)


if __name__ == '__main__':
  try:
    sys.exit(download_and_unpack(CURRENT_SDK))
  except KeyboardInterrupt:
    logger.warning("KeyboardInterrupt")
    sys.exit(1)
