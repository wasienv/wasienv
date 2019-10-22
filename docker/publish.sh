#!/bin/bash

DIR="$( cd "$( dirname "$0" )" && pwd )"

docker build $DIR -t wasienv/wasienv
docker push wasienv/wasienv:latest
