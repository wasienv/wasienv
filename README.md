# WASIc: The WASI Compiler Toolchain

WASIc is a toolchain for compiling to WebAssembly WASI, that let you compile C/C++ projects easily to WASI, so you can run them anywhere (in the Browsers, or with any Standalone WASI WebAssembly runtime).

> Note: If you aim to use the WebAssembly files in the web directly (using graphics, audio or other tools that are not supported in WASI) then [Emscripten](https://emscripten.org/) is probably a much better choice.

## Install

You can install `wasic` with:

```
curl https://raw.githubusercontent.com/wasic-core/wasic/master/install.sh | sh
```

## Using WASIc

If you want to compile a file to a WebAssembly WASI:

```bash
# To compile to a WebAssembly WASI file
# This command will generate:
#  • A executable: ./example
#  • A WebAssembly file: ./example.wasm
wasicc examples/example.c -o example

# If you are using configure
wasiconfigure ./configure

# If you are using cmake (or make)
wasimake cmake .
```

## Commands

When installing `wasic`, the following commands will be automatically avialable:

### `wasic`

This is the compiler toolchain. You have two commands available:

For installing a SDK (`wasic install-sdk`):

```bash
wasic install-sdk 7
```

For setting a SDK as the default (`wasic default-sdk`):

```bash
wasic default-sdk 7
```

### `wasicc`

It's a wrapper on top of `clang`, with additions for the stubs, sysroot and target.
It also detects autoexecutables in the output and wraps to execute them with a WebAssembly WASI runtime via `wasirun`.

### `wasic++`

It's a wrapper on top of `clang++`, with additions for the stubs, sysroot and target.
It also detects autoexecutables in the output and wraps to execute them with a WebAssembly WASI runtime via `wasirun`.

### `wasiconfigure`

It's a helper that adds the WASIc environment vars (`CC`, `CXX`, `RUNLIB`, ...) to the following command (`./configure`).

Example:

```bash
wasiconfigure ./configure
```

### `wasimake`

It's a helper that adds the WASIc environment vars (`CC`, `CXX`, `RUNLIB`, ...) for the make (`make` or `cmake`).

Example:

```bash
# With CMake
wasimake cmake .

# With Make
wasimake make
```

### `wasirun`

It executes a given WebAssembly file with a standalone WebAssembly runtime.

```bash
wasirun myfile.wasm
```

## Contributing

After cloning this repo, ensure dependencies are installed by running:

```bash
python setup.py develop
```

After that, all the commands will be available on your shell and you should be able to start seeing the changes directly without re-installing wasic.


## How WASIc compares to ...?

### Emscripten

[Emscripten](https://emscripten.org/) is a great toolchain that let's you compile your C/C++ projects to WebAssembly so you can use them in the web easily.

However, Emscripten has a **non-stable ABI** (beacuse they need constant and fast iteration).
This makes it a bit challening for standalone-runtimes to continually adapt.
Because of that, adopting the WASI ABI is a much easier path for standalone sever-side Wasm runtimes.

Right now Emscripten is moving towards WASI adoption. However is not yet possible to create WASI-only Wasm files since they are doing a gradual approach.
Emscripten has also some tools that are not needed in the case of sever-side Standalone WebAssembly runtimes, such as [`EM_ASM`](https://emscripten.org/docs/porting/connecting_cpp_and_javascript/Interacting-with-code.html#calling-javascript-from-c-c).

WASIc learns a lot from Emscripten, since they figured out the perfect ergonomics for having C/C++ projects to adopt WebAssembly. Alon, the creator of Emscripten is without any doubt, one of the brilliant minds behind WebAssembly and he inspired us with his work to keep improving the ergonomics of WASI.

### WASI-libc

WASI-libc is the "frontend ABI" for WASI. By itself, it only provide header files and implementations that make C compilers adopt WASI very easily via the `--sysroot` flag.

### WASI-SDK

WASI-SDK is the union between `WASI-libc` and the compiler binaries `clang`, `wasm-ld`, ...

WASIc is using WASI-SDK under the hood to compile to WebAssembly, however it differs from it in two major ways:
* WASIc is designed to work with **multiple SDKs** versions at the same time
* WASIc is completely focused on the **ergonomics**, exposing very simple to use CLI tools so projects can adopt it easily.

We can see of WASIc as the merge between Emscripten and the WASI-SDK.
