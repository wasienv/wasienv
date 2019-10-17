import os

from sdk import WASI_SDK_DIR

wasienv_DIR    = os.path.dirname(__file__)

# The location of the underlying binaries
CC      = os.path.join(WASI_SDK_DIR, "bin/clang")
LD      = os.path.join(WASI_SDK_DIR, "bin/wasm-ld")
CXX     = os.path.join(WASI_SDK_DIR, "bin/clang++")
NM      = os.path.join(WASI_SDK_DIR, "bin/llvm-nm")
AR      = os.path.join(WASI_SDK_DIR, "bin/llvm-ar")
RANLIB  = os.path.join(WASI_SDK_DIR, "bin/llvm-ranlib")

WASI_SYSROOT = os.path.join(WASI_SDK_DIR, "share/wasi-sysroot")

# Binaries
WASI_CC      = "wasicc"
WASI_CXX     = "wasic++"
WASI_LD      = "wasild"
WASI_AR      = "wasiar"
WASI_NM      = "wasinm"
WASI_RANLIB  = "wasiranlib"
WASI_RUN  = "wasirun"

WASI_CMAKE   = os.path.abspath(os.path.join(wasienv_DIR, "wasienv.cmake"))

STUBS_SYSTEM_LIB = os.path.join(wasienv_DIR, "stubs")
STUBS_SYSTEM_PREAMBLE = os.path.join(STUBS_SYSTEM_LIB, "preamble.h")
