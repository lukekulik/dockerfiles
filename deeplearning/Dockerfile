FROM ubuntu:16.04

MAINTAINER Luke Kulik

RUN apt-get update && apt-get install -y --no-install-recommends \
        software-properties-common

RUN add-apt-repository ppa:fkrull/deadsnakes

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git \
        vim \
        libfreetype6-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        python \
        python-dev \
        python3.6 \
        python3.6-dev \
        rsync \
        unzip \
        wget \
        tmux \
        libavcodec-dev \
        libavformat-dev \
        libswscale-dev \
        libgtk2.0-dev \
        libatlas-base-dev \
        gfortran\
        libv4l-dev\
        libjpeg8-dev \
        libtiff5-dev \
        libjasper-dev \
        libpng12-dev \
        libjpeg-dev \
        libopenblas-dev \
        liblapack-dev \
        unrar \
        cmake \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
RUN update-alternatives --config python3

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

# Install PyTorch
RUN pip --no-cache-dir install \
    http://download.pytorch.org/whl/cu80/torch-0.2.0.post3-cp27-cp27mu-manylinux1_x86_64.whl
RUN pip3 --no-cache-dir install \
    http://download.pytorch.org/whl/cu80/torch-0.2.0.post3-cp36-cp36m-manylinux1_x86_64.whl

RUN pip --no-cache-dir install \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        scipy \
        sklearn \
        pandas \
        pillow-simd \
        keras \
        bcolz \
        futures \
        torchvision \
        tensorflow \
        h5py \
        awscli \
        satpy \
        h5netcdf \
        opencv-python \
        cython \
        theano \
        && \
    python -m ipykernel.kernelspec

RUN pip3 --no-cache-dir install \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        scipy \
        sklearn \
        pandas \
        pillow-simd \
        keras \
        bcolz \
        futures \
        torchvision \
        tensorflow \
        h5py \
        awscli \
        satpy \
        h5netcdf \
        tqdm \
        graphviz \
        visdom \
        opencv-python \
        cython \
        theano \
        && \
    python3 -m ipykernel.kernelspec
  
# --- DO NOT EDIT OR DELETE BETWEEN THE LINES --- #
# These lines will be edited automatically by parameterized_docker_build.sh. #
# COPY _PIP_FILE_ /
# RUN pip --no-cache-dir install /_PIP_FILE_
# RUN rm -f /_PIP_FILE_

RUN ln -s /usr/bin/python3 /usr/bin/python#

# Set up our notebook config.
COPY jupyter_notebook_config.py /root/.jupyter/

# Copy sample notebooks.
COPY notebooks /notebooks

# Jupyter has issues with being run directly:
#   https://github.com/ipython/ipython/issues/7062
# We just add a little wrapper script.
COPY run_jupyter.sh /

# For CUDA profiling, TensorFlow requires CUPTI.
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888

WORKDIR "/workspace"
