# wasienv examples

### Simple C file

You can compile the `example.c` file into WebAssembly with `wasicc`:

```bash
wasicc example.c -o example
```

This will create:
* `example.wasm` file with the WebAssembly contents
* `example` executable that runs `example.wasm` with a WebAssembly runtime

### CMake project

If you are working with CMake, you just need to wrap the `cmake` call with `wasimake`.
Example:

```bash
# Before
cmake .

# After
wasimake cmake .
```

> Note: The project [c-wasm-simd128-example](https://github.com/wasmerio/c-wasm-simd128-example) showcases very easily how to use it

### Autoconf project

If your project is using Autoconf, you just need to wrap the calls to `./configure` and `make` with `wasiconfigure` and `wasimake` respectively. Example:

```bash
# Before
./configure
make

# After
wasiconfigure ./configure
wasimake make
```

> Note: The project [jq](https://github.com/wapm-packages/jq) showcases very easily how to use it.
