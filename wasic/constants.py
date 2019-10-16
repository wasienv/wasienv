import os

from sdk import WASI_SDK_DIR

WASIC_DIR    = os.path.dirname(os.path.dirname(__file__))

# The location of the underlying binaries
CC      = os.path.join(WASI_SDK_DIR, "bin/clang")
LD      = os.path.join(WASI_SDK_DIR, "bin/wasm-ld")
CXX     = os.path.join(WASI_SDK_DIR, "bin/clang++")
NM      = os.path.join(WASI_SDK_DIR, "bin/llvm-nm")
AR      = os.path.join(WASI_SDK_DIR, "bin/llvm-ar")
RANLIB  = os.path.join(WASI_SDK_DIR, "bin/llvm-ranlib")

WASI_SYSROOT = os.path.join(WASI_SDK_DIR, "share/wasi-sysroot")

# Binaries
# WASI_CC      = os.path.join(WASIC_DIR, "bin/wasicc")
# WASI_CXX     = os.path.join(WASIC_DIR, "bin/wasic++")
# WASI_LD      = os.path.join(WASIC_DIR, "bin/wasild")
# WASI_AR      = os.path.join(WASIC_DIR, "bin/wasiar")
# WASI_NM      = os.path.join(WASIC_DIR, "bin/wasinm")
# WASI_RANLIB  = os.path.join(WASIC_DIR, "bin/wasiranlib")
WASI_CC      = "wasicc"
WASI_CXX     = "wasic++"
WASI_LD      = "wasild"
WASI_AR      = "wasiar"
WASI_NM      = "wasinm"
WASI_RANLIB  = "wasiranlib"
WASI_RUN  = "wasirun"

WASI_CMAKE   = os.path.abspath(os.path.join(WASIC_DIR, "wasic.cmake"))

STUBS_SYSTEM_LIB = os.path.join(WASIC_DIR, "stubs")
STUBS_SYSTEM_PREAMBLE = os.path.join(STUBS_SYSTEM_LIB, "preamble.h")
