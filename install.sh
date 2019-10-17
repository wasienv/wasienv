#!/bin/sh

# This install script is intended to download and install the latest available
# release of wasienv.

# You can install using this script:
# $ curl https://raw.githubusercontent.com/wasienv/wasienv/master/install.sh | sh

set -e
reset="\033[0m"
blue="\033[44m"
m="\033[34;1m"
bold="\033[1m"
green="\033[32m"

echo "
${m}┏━━━━━━━━━┓${reset}
${m}┃         ┃${reset}
${m}┃   ${reset}${bold}wasi${m} (${reset} ${bold}env${reset}
${m}┃         ┃${reset}
${m}┗━━━━━━━━━┛${reset}
"

echo "${green}${bold}> Installing wasienv${reset}"
pip install wasienv --upgrade || pip install wasienv --user --upgrade

echo "\n${green}${bold}> Installing a WebAssembly WASI Runtime${reset}"
curl https://get.wasmer.io -sSfL | sh

echo "\n${green}${bold}> Installing the required WASI SDKs${reset}"
# unstable is the most stable version of the WASI sdk for now
wasienv install-sdk unstable
wasienv default-sdk unstable
