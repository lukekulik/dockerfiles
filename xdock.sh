if [ ${1:-$choice} = "cpu" ]; then
	docker run --rm  -v /net/d13/data/lkulik/:/workspace:Z -p 8888:8888 -p 6006:6006 -ti lkulik/deeplearning-cpu
fi

if [ ${1:-$choice} = "gpu" ]; then
	nvidia-docker run --rm  -v /data/lkulik/:/workspace:Z -p 8888:8888 -p 6006:6006 -ti --shm-size 20G lkulik/deeplearning-gpu
fi
