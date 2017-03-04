srun -c1 --pty --gres=gpu:1 nvidia-docker run --rm -v ~/work/:/work -v ~/models/:/models -ti tensorflow python /work/TensorFlow-Examples/examples/3_NeuralNetworks/autoencoder.py
