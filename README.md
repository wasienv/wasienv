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
wasicc example.c -o example

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
It also detects autoexecutables in the output and wraps to execute them with a WebAssembly WASI runtime.

### `wasic++`

It's a wrapper on top of `clang++`, with additions for the stubs, sysroot and target.
It also detects autoexecutables in the output and wraps to execute them with a WebAssembly WASI runtime.

### `wasiconfigure`

It's a helper that adds the WASIc environment vars (`CC`, `CXX`, `RUNLIB`, ...) to the following command (`./configure`).

Example:

```bash
wasiconfigure ./configure
```

### `wasimake`

It's a helper that adds the WASIc environment vars (`CC`, `CXX`, `RUNLIB`, ...) for the make (`make` or `cmake`).
s
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
