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

from .tools import logger, run_process

# Where the python packages live
PACKAGES_DIR    = os.path.dirname(os.path.dirname(__file__))

# Where the wasienv storage lives
WASI_STORAGE_DIR    = os.path.join(PACKAGES_DIR, "wasienv-storage")
WASI_SDKS_DIR = os.path.join(WASI_STORAGE_DIR, "sdks")

WASI_SWIFT_DIR = os.path.join(WASI_STORAGE_DIR, "swift")
# THe dir where the specific environment for swiftenv lives
WASI_SWIFT_ENV_DIR = os.path.join(WASI_SWIFT_DIR, "env")
# The dir where swiftenv lives
WASI_SWIFTENV_DIR = os.path.join(WASI_SWIFT_DIR, "swiftenv")

CURRENT_SDK = "14"

SDKS = {
    "5": {
        "download_urls": {
            "darwin": 'https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-5/wasi-sdk-5.0-macos.tar.gz',
            "linux": 'https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-5/wasi-sdk-5.0-linux.tar.gz',
        },
        "sysroot": "wasi-sdk-5.0/opt/wasi-sdk"
    },
    "6": {
        "download_urls": {
            "darwin": 'https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-6/wasi-sdk-6.0-macos.tar.gz',
            "linux": 'https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-6/wasi-sdk-6.0-linux.tar.gz',
        },
        "sysroot": "wasi-sdk-6.0/opt/wasi-sdk"
    },
    "7": {
        "download_urls": {
            "darwin": 'https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-7/wasi-sdk-7.0-macos.tar.gz',
            "linux": 'https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-7/wasi-sdk-7.0-linux.tar.gz',
        },
        "sysroot": "wasi-sdk-7.0/opt/wasi-sdk"
    },
    "8": {
        "download_urls": {
            "darwin": 'https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-8/wasi-sdk-8.0-macos.tar.gz',
            "linux": 'https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-8/wasi-sdk-8.0-linux.tar.gz',
        },
        "sysroot": "wasi-sdk-8.0"
    },
    "10": {
        "download_urls": {
            "darwin": 'https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-10/wasi-sdk-10.0-macos.tar.gz',
            "linux": 'https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-10/wasi-sdk-10.0-linux.tar.gz',
        },
        "sysroot": "wasi-sdk-10.0"
    },
    "14": {
        "download_urls": {
            "darwin": 'https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-14/wasi-sdk-14.0-macos.tar.gz',
            "linux": 'https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-14/wasi-sdk-14.0-linux.tar.gz',
        },
        "sysroot": "wasi-sdk-14.0"
    },
}

SDK_TAGS = {
    "latest": "14",
    "unstable": "14"
}

SWIFTWASM = {
    "dev-2020-03-18": {
        "download_urls": {
            "darwin": "https://github.com/swiftwasm/swift/releases/download/swift-wasm-DEVELOPMENT-SNAPSHOT-2020-03-18-a/swift-wasm-DEVELOPMENT-SNAPSHOT-2020-03-18-a-osx.tar.gz",
            "linux": "https://github.com/swiftwasm/swift/releases/download/swift-wasm-DEVELOPMENT-SNAPSHOT-2020-03-08-a/swift-wasm-DEVELOPMENT-SNAPSHOT-2020-03-18-a-linux.tar.gz",
        },
        "codename": "wasm-DEVELOPMENT-SNAPSHOT-2020-03-18-a"
    }
}

SWIFTWASM_TAGS = {
    "latest": "dev-2020-03-18"
}

SWIFTENV_BIN = os.path.join(WASI_SWIFTENV_DIR, "bin", "swiftenv")


class SDKException(Exception):
    pass


class SDKAlreadyExists(SDKException):
    pass


class SDKNotInstalled(SDKException):
    pass


def get_sdk_dir(sdk_name):
    return os.path.join(WASI_SDKS_DIR, sdk_name)


def unalias_name(sdk_name, on=SDK_TAGS):
    if sdk_name in on:
        sdk_name = on[sdk_name]
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


def dir_full(directory):
    return os.path.exists(directory) and os.path.isdir(directory) and bool(os.listdir(directory))


def dir_create(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            return
        else:
            raise Exception("The path {} is a file. Can't create dir".format(path))
    os.makedirs(path)


def dir_delete(path):
    if not os.path.exists(path):
        return
    if os.path.isdir(path):
        os.rmdir(path)
    else:
        os.rm(path)

def is_swiftenv_installed():
    return dir_full(WASI_SWIFTENV_DIR)


def install_swiftenv():
    try:
        run_process(["swiftc", "-v"])
    except:
        raise Exception("Can't find the swiftc program in your system. Is needed for the WASI Swift installation")

    dir_create(WASI_SWIFT_DIR)
    print("Installing Swiftenv in {}".format(WASI_SWIFTENV_DIR))
    dir_delete(WASI_SWIFTENV_DIR)
    run_process(["git","clone","https://github.com/kylef/swiftenv.git",WASI_SWIFTENV_DIR])
    print("Swiftenv installed successfully")
    os.environ["SWIFTENV_ROOT"] = WASI_SWIFT_ENV_DIR


def install_swiftwasm(version):
    if not is_swiftenv_installed():
        install_swiftenv()
    version = version or "latest"
    version_tag = unalias_name(version, on=SWIFTWASM_TAGS)
    system = platform.system()
    swiftwasm_version = SWIFTWASM.get(version_tag)
    download_urls = swiftwasm_version.get("download_urls", {})
    download_url = download_urls.get(system.lower(), None)
    os.environ["SWIFTENV_ROOT"] = WASI_SWIFT_ENV_DIR
    code = run_process([SWIFTENV_BIN, "install", download_url], check=False)
    if code:
        print("There has been an issue installing the latest SDK")


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
