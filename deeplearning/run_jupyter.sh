#!/usr/bin/env bash

jupyter notebook --port 8888 --allow-root  >> /jupyter.log 2>&1  &
tensorboard --logdir=/workspace/runs/ >> /tensorboard.log 2>&1  &
