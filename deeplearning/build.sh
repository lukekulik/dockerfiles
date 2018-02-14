#!/usr/bin/env bash

choice="both"


if [ ${1:-$choice} = "cpu" ]; then
    docker build -t lkulik/deeplearning-cpu -f Dockerfile .
fi

if [ ${1:-$choice} = "gpu" ]; then
    nvidia-docker build -t lkulik/deeplearning-gpu -f Dockerfile.gpu .
fi
if [ ${1:-$choice} = "both" ]; then
    nvidia-docker build -t lkulik/deeplearning-gpu -f Dockerfile.gpu .
    docker build -t lkulik/deeplearning-cpu -f Dockerfile .
fi
