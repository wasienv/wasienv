#!/bin/sh

# This install script is intended to download and install the latest available
# release of wasienv.

# You can install using this script:
# $ curl https://raw.githubusercontent.com/wasienv/wasienv/master/install.sh | sh

set -e
echo "Installing wasienv"
pip install wasienv --upgrade || pip install wasienv --user --upgrade

echo "Installing a WebAssembly WASI Runtime"
curl https://get.wasmer.io -sSfL | sh

echo "Installing the required WASI SDKs"
# unstable is the most stable version of the WASI sdk for now
wasienv install-sdk unstable
wasienv default-sdk unstable
