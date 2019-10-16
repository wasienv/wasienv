#!/bin/sh

# This install script is intended to download and install the latest available
# release of WASIc.

# You can install using this script:
# $ curl https://raw.githubusercontent.com/wasic-core/wasic/master/install.sh | sh

set -e
pip install --user wasic --upgrade

# unstable is the most stable version of the WASI sdk for now
wasic install-sdk unstable
wasic default-sdk unstable
