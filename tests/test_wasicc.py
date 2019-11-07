import os

from wasienv.wasicc import run
from wasienv.tools import is_exe, is_wasm 

EXAMPLES_DIR = os.path.join(os.path.dirname(__file__), '../examples/')
os.chdir(EXAMPLES_DIR)


def test_wasicc():
    return_code = run(["wasicc", "c/example-wasi.c", "-o", "c/example-wasi"])
    assert return_code == 0
    assert is_exe("c/example-wasi")
    assert is_wasm("c/example-wasi.wasm")


def test_wasicpp():
    return_code = run(["wasic++", "cpp/example-wasi.cpp", "-o", "cpp/example-wasi"])
    assert return_code == 0
    assert is_exe("cpp/example-wasi")
    assert is_wasm("cpp/example-wasi.wasm")
