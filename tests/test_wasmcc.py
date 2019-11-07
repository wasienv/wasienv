import os

from wasienv.wasmcc import run
from wasienv.tools import is_exe, is_wasm 

EXAMPLES_DIR = os.path.join(os.path.dirname(__file__), '../examples/')
os.chdir(EXAMPLES_DIR)


def test_wasicc():
    return_code = run(["wasmcc", "c/example-wasm.c", "-o", "c/example-wasm"])
    assert return_code == 0
    assert is_exe("c/example-wasm")
    assert is_wasm("c/example-wasm.wasm")


def test_wasicpp():
    return_code = run(["wasmc++", "cpp/example-wasm.cpp", "-o", "cpp/example-wasm"])
    assert return_code == 0
    assert is_exe("cpp/example-wasm")
    assert is_wasm("cpp/example-wasm.wasm")
