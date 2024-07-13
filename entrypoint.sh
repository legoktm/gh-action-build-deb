#!/bin/bash

docker build -f /inner/Dockerfile -t inner \
    --build-arg DISTRO="$INPUT_DISTRO" .
docker run --rm -v /github/workspace:/github/workspace \
    --workdir=$(pwd) inner
