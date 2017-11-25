#!/usr/bin/env bash

if [ $1 = "cpu" ]; then
    docker build -t lkulik/deeplearning-cpu -f Dockerfile .
fi

if [ $1 = "gpu" ]; then
    nvidia-docker build -t lkulik/deeplearning-gpu -f Dockerfile.gpu .
fi
