FROM nvcr.io/nvidia/torch:17.02
MAINTAINER Fangchang Ma <fcma@mit.edu>

# ubuntu packages
RUN apt-get update && apt-get install -y \
  git \
  wget \ 
  unzip \ 
  vim \
  libmatio2
#  tmux \
#  libopenblas-dev \
#  liblapack-dev
#  cython \
#  gnuplot 
  
# python packages
# RUN pip install h5py

# Torch packages
# RUN luarocks install torchx 
RUN luarocks install torch
RUN luarocks install matio
# RUN luarocks install nnx
# RUN luarocks install hdf5
# RUN luarocks install csvigo
# RUN luarocks install colormap

# enviromnet
ENV OMP_NUM_THREADS=2
