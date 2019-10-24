<p align="center">
  <a href="https://github.com/wasienv/wasienv" target="_blank" rel="noopener noreferrer">
    <img height="180" src="https://raw.githubusercontent.com/wasienv/wasienv/master/logo.png" alt="Wasienv logo">
  </a>
</p>

<p align="center">
  <a href="https://github.com/wasmerio/wasmer/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/wasienv/wasienv.svg?style=flat-square" alt="License">
  </a>
</p>

# Wasienv: WASI Development Toolchain for C/C++

Wasienv is a tool that aims to bring all projects to [WebAssembly WASI](https://github.com/WebAssembly/WASI). With `wasienv` you can compile C/C++ projects easily to WASI, so you can run them anywhere (with any Standalone WASI WebAssembly runtime, or [in the Browser](https://webassembly.sh)).

> Note: If you aim to use the WebAssembly files in the web directly (using graphics, audio or other tools that are not supported in WASI) then [Emscripten](https://emscripten.org/) is probably a much better choice.

## Install

You can install `wasienv` with:

```sh
curl https://raw.githubusercontent.com/wasienv/wasienv/master/install.sh | sh
```

> Note: we also ship `wasienv` in a Docker image. You can check [how to use the Wasienv Docker image here](https://github.com/wasienv/wasienv/blob/master/docker/).

## Using wasienv

If you want to compile a C file to a WebAssembly WASI:

```sh
# To compile to a WebAssembly WASI file
# This command will generate:
#  • An executable: ./example
#  • A WebAssembly file: ./example.wasm
wasicc examples/example.c -o example

# If you are using configure
wasiconfigure ./configure

# If you are using cmake (or make)
wasimake cmake .
```

## Commands

When installing `wasienv`, the following commands will be automatically available:

### `wasienv`

This is the compiler toolchain. You have two commands available:

For installing a SDK (`wasienv install-sdk`):

```sh
wasienv install-sdk 7
```

For setting a SDK as the default (`wasienv default-sdk`):

```sh
wasienv default-sdk 7
```

### `wasicc`

It's a wrapper on top of `clang`, with additions for the stubs, sysroot and target.
It also detects autoexecutables in the output and wraps to execute them with a WebAssembly WASI runtime via `wasirun`.

### `wasic++`

It's a wrapper on top of `clang++`, with additions for the stubs, sysroot and target.
It also detects autoexecutables in the output and wraps to execute them with a WebAssembly WASI runtime via `wasirun`.

### `wasiconfigure`

It's a helper that adds the wasienv environment vars (`CC`, `CXX`, `RUNLIB`, ...) to the following command (`./configure`).

Example:

```sh
wasiconfigure ./configure
```

### `wasimake`

It's a helper that adds the wasienv environment vars (`CC`, `CXX`, `RUNLIB`, ...) for the make (`make` or `cmake`).

Example:

```sh
# With CMake
wasimake cmake .

# With Make
wasimake make
```

### `wasirun`

It executes a given WebAssembly file with a standalone WebAssembly runtime.

```sh
wasirun myfile.wasm
```

## Contributing

After cloning this repo, ensure dependencies are installed by running:

```sh
python setup.py develop
```

After that, all the commands will be available on your shell and you should be able to start seeing the changes directly without re-installing wasienv.


## How wasienv compares to …?

### Emscripten

[Emscripten](https://emscripten.org/) is a great toolchain that let's you compile your C/C++ projects to WebAssembly so you can use them in the web easily.

However, Emscripten has a **non-stable ABI** (because constant and fast iteration is very useful for their usecase).
This makes it a bit challening for standalone-runtimes to continually adapt.
Because of that, adopting the WASI ABI is a much easier path for standalone server-side WebAssembly runtimes.

Right now Emscripten is [moving towards WASI adoption](https://github.com/emscripten-core/emscripten/issues/9479). 
However, Emscripten can only emit WASI WebAssembly files for some programs as Emscripten's filesystem layer supports POSIX features not yet present in WASI.

Emscripten has also some tools that are not needed (nor supported) in the case of server-side Standalone WebAssembly runtimes, such as [`EM_JS` and `EM_ASM`](https://emscripten.org/docs/porting/connecting_cpp_and_javascript/Interacting-with-code.html#calling-javascript-from-c-c).

Wasienv learns a lot from Emscripten, since they figured out the perfect ergonomics for having C/C++ projects to adopt WebAssembly. Alon, the creator of Emscripten, is without any doubt one of the brilliant minds behind WebAssembly and he inspired us with his work to keep improving the ergonomics of WASI.

### WASI-libc

WASI-libc is the "frontend ABI" for WASI. By itself, it only provides header files and implementations that make C compilers adopt WASI very easily via the `--sysroot` flag.

### WASI-SDK

We can see WASI-SDK as the union between `WASI-libc` and the compiler binaries `clang`, `wasm-ld`, ...

Wasienv is using WASI-SDK under the hood to compile to WebAssembly, however it differs from it in two major ways:
1. `wasienv` is designed to work with **multiple SDKs** versions
2. `wasienv` is completely focused on the **ergonomics**, exposing very simple to use CLI tools so that projects can adopt it easily.

We can think of `wasienv` as applying the ergonomic ideas from Emscripten to the WASI-SDK
