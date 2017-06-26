FROM compute.nvidia.com/nvidia/torch

# ubuntu packages
RUN apt-get update && apt-get install -y \
  wget \ 
  unzip \ 
  vim \
  tmux \
  libmatio2 \
  libopenblas-dev \
  liblapack-dev \
  cython \
  gnuplot 
  
# python packages
RUN pip install h5py

# torch packages
RUN luarocks install torchx 
RUN luarocks install matio
RUN luarocks install hdf5
RUN luarocks install csvigo
RUN luarocks install colormap

# enviromnet
ENV OMP_NUM_THREADS=2
