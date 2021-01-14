FROM debian:buster AS stage_build


RUN echo "## Update and install packages"
RUN apt-get update
RUN apt-get install -y --no-install-recommends python python-pip python-setuptools python-wheel curl
RUN echo "## Done"

RUN echo "## Installing CMake"
RUN curl https://cmake.org/files/v3.17/cmake-3.17.1-Linux-x86_64.sh --output cmake-3.17.1-Linux-x86_64.sh \
    &&  mkdir /opt/cmake \
    &&  printf "y\nn\n" | sh cmake-3.17.1-Linux-x86_64.sh --prefix=/opt/cmake > /dev/null \
    &&  ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake
RUN echo "## Done"

RUN echo "## Installing wasienv"
RUN curl https://raw.githubusercontent.com/wasienv/wasienv/master/install.sh | sh

ENV WASIENV_DIR="/root/.wasienv"

ENV WASMER_DIR="/root/.wasmer"
ENV WASMER_CACHE_DIR="$WASMER_DIR/cache"

ENV PATH="$WASMER_DIR/bin:$WASIENV_DIR/bin:$PATH:$WASMER_DIR/globals/wapm_packages/.bin"

RUN echo "## Done"
