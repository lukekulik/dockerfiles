FROM compute.nvidia.com/nvidia/torch
# FROM nvidia/cuda:8.0-cudnn7-devel-ubuntu14.04
MAINTAINER Fangchang Ma <fcma@mit.edu>

# ubuntu packages
RUN apt-get update && apt-get install -y \
  git \
  wget \ 
  unzip \ 
  vim \
  tmux \
  libmatio2 \
  libopenblas-dev \
  liblapack-dev
#  cython \
#  gnuplot 
  
# python packages
# RUN pip install h5py

# Cuda
RUN mkdir /root/cuda
WORKDIR /root/cuda
RUN wget https://www.dropbox.com/s/j4rva5lnllittw6/cuda-repo-ubuntu1404_8.0.61-1_amd64.deb && \
  dpkg -i cuda-repo-ubuntu1404_8.0.61-1_amd64.deb
RUN apt-get update && apt-get install --no-install-recommends -y cuda

# Torch and luarocks
RUN git clone https://github.com/torch/distro.git /root/torch --recursive && \ 
  cd /root/torch && \
  bash install-deps && \
  ./install.sh -b

ENV LUA_PATH='/root/.luarocks/share/lua/5.1/?.lua;/root/.luarocks/share/lua/5.1/?/init.lua;/root/torch/install/share/lua/5.1/?.lua;/root/torch/install/share/lua/5.1/?/init.lua;./?.lua;/root/torch/install/share/luajit-2.1.0-beta1/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua'
ENV LUA_CPATH='/root/.luarocks/lib/lua/5.1/?.so;/root/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so'
ENV PATH=/root/torch/install/bin:$PATH
ENV LD_LIBRARY_PATH=/root/torch/install/lib:$LD_LIBRARY_PATH
ENV DYLD_LIBRARY_PATH=/root/torch/install/lib:$DYLD_LIBRARY_PATH
ENV LUA_CPATH='/root/torch/install/lib/?.so;'$LUA_CPATH

# Torch packages
# RUN luarocks install torchx 
RUN luarocks install matio
# RUN luarocks install hdf5
# RUN luarocks install csvigo
# RUN luarocks install colormap

# Cuda
# RUN apt-get install --no-install-recommends -y cuda
# RUN luarocks install FindCUDA
# RUN luarocks install cutorch
# RUN luarocks install cunn
# RUN luarocks install cudnn

WORKDIR /workspace

# enviromnet
ENV OMP_NUM_THREADS=2
