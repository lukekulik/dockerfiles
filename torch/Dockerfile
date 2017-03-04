FROM compute.nvidia.com/nvidia/torch

#update
RUN apt-get update

# data packages
RUN apt-get install -y wget unzip

# util packages
RUN apt-get install -y vim tmux libmatio2

# torch packages
RUN luarocks install torchx
RUN luarocks install matio

# enviromnet
ENV OMP_NUM_THREADS=2
