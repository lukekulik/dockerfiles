#!/usr/bin/env bash

if [ $0 = "cpu" ]; then
    docker build -t lkulik/deeplearning-cpu -f Dockerfile.cpu .
fi

if [ $0 = "gpu" ]; then
    nvidia-docker build -t lkulik/deeplearning-gpu -f Dockerfile.gpu .
fi
