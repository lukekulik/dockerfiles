srun -c1 --pty --gres=gpu:1 nvidia-docker run --rm -v ~/work/:/work -ti tensorflow python /work/TensorFlow-Examples/examples/1_Introduction/helloworld.py
