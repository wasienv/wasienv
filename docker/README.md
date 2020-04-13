# Wasienv - Docker

<!-- This docs are inspired from: https://raw.githubusercontent.com/trzecieu/emscripten-docker/master/docs/emscripten.md -->

Based on: **debian:stretch-slim**

[![Docker Pulls](https://img.shields.io/docker/pulls/wasienv/wasienv.svg?style=flat-square)](https://store.docker.com/community/images/wasienv/wasienv/) [![Size](https://images.microbadger.com/badges/image/wasienv/wasienv.svg)](https://microbadger.com/images/wasienv/wasienv/)

The minimal version that is required to compile C++ code with [wasienv](https://github.com/wasienv/wasienv) to WebAssembly (Wasm). The goal was to provide the best and the most lightweight foundation for custom Docker images.
Each tag was build from single [Dockerfile](https://github.com/wasienv/wasienv/blob/master/docker/Dockerfile)

## Packages

### Manually installed:

|packages|version|
|---|---|
|`cmake`|**3.17.1**|

### System installed:

|packages|version|
|---|---|
|`python`|**2.7.17**|
|`python-pip`|**18.1.5**|
|`python-setuptools`|**41.2.0**|
|`python-wheel`|**0.33.6**|
|`curl`|**7.66**|

<!-- installed_packages -->

## Tag schema
|tag|description|
|--|--|
|`latest`|The default version (aka `latest`) points at [the latest tag release](https://github.com/wasienv/wasienv/releases) by Wasienv.|

## Usage
From start every Wasienv command is available. For the instance: `wasicc`, `wasic++`, `wasimake`, `wasiar`, `wasmer`, `wasi` etc.

To compile a single file:
```bash
docker run --rm -v `pwd`:`pwd` wasienv/wasienv wasic++ `pwd`/helloworld.cpp -o `pwd`/helloworld.wasm
```

More elaborated Hello World:
```bash
# create helloworld.cpp
cat << EOF > helloworld.cpp
#include <iostream>
int main() {
  std::cout << "Hello World!" << std::endl;
  return 0;
}
EOF

# compile with docker image
docker run \
  --rm \
  -v $(pwd):$(pwd) \
  -u $(id -u):$(id -g) \
  wasienv/wasienv \
  wasic++ `pwd`/helloworld.cpp -o `pwd`/helloworld.wasm

# execute on host machine
wasmer run helloworld.wasm
```

Teardown of compilation command:

|part|description|
|---|---|
|`docker run`| A standard command to run a command in a container|
|`--rm`|remove a container after execution (optimization)|
|`-v $(pwd):$(pwd)`|Mounting current folder from the host system into mirrored path on the container<br>TIP: This helps to investigate possible problem as we preserve exactly the same paths like in host. In such case modern editors (like Sublime, Atom, VS Code) let us to CTRL+Click on a problematic file |
|`-u $(id -u):$(id -g)`|(1.37.23+) Run a container as a non-root user with the same UID and GID as local user. Hence all files produced by this are accessible to non-root users|
|`wasienv/wasienv`|Get the latest tag of this container|
|`wasicc helloworld.cpp -o helloworld.wasm`|Execute `wasicc` command with following arguments inside container, effectively compile our source code|

## Extending this image
If you would like to extend this image you have two choices:
### Extend with keeping base image
An example how to derive from base image and keep linux base container you can find here : [wasienv/wasienv/Dockerfile](https://github.com/wasienv/wasienv/blob/master/docker/Dockerfile).

All what you need is:
```Dockerfile
FROM wasienv/wasienv:latest

RUN ...
```
This way you inherit all settings of environment that are coming with this image and entrypoiont.

## Build this image manually

0. Pull the latest https://github.com/wasienv/wasienv
0. Navigate to wanted flavor to compile inside `./docker` path, let's say `./docker/`.
0. Execute singe docker command and provide wanted version to compile as an argument:
```bash
docker build -t my_little_wasienv_image --build-arg  .
```

## License
[![MIT](https://img.shields.io/github/license/wasienv/wasienv.svg?style=flat-square)](https://github.com/wasienv/wasienv/blob/master/LICENSE)
