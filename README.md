# dockerfiles
dockerfiles for [Docker](https://www.docker.com/), a software container platform.

## Installation
Assume that [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) has been installed and that this repo is located under the home folder `~/dockerfiles/`.

	## choose an <image-name> for yourself
    $ cd ~/dockerfiles/<image-name>
    $ nvidia-docker build -t <image-name> . 

Alternatively, if a `build.sh` script exists in the folder, then simply run 

	## choose an <image-name> for yourself
	$ cd ~/dockerfiles/<image-name>
	$./build.sh

Note: Docker files under `/dockerfiles/dgx-1` are images optimzed for [NVIDIA DGX-1](https://www.nvidia.com/en-us/data-center/dgx-1/) and requires an NVIDIA DGX Cloud Services account to access the DGX™ Container Registry. See [Installing Docker and NVIDIA Docker](http://docs.nvidia.com/deeplearning/dgx/quick-start-guide/index.html#installdocker) for details.

## Usage

	## launch the docker image in an interactive session, and mount the home foler ~/ inside the container at /workspace 
    $ nvidia-docker run --rm -v ~/:/workspace -ti <image-name>

