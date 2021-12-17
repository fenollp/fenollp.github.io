---
published: true
title: Train reinforcement learning baselines on manycore
layout: post
categories: [projects, rl, gym, docker_host]
permalink: train_reinforcement-learning_baselines_on_manycore
---

In conjonction with the *solar 3D printer / sand melter machine* and the `DOCKER_HOST=... docker build ...` service I am working on (among many other things!)
I need to be able to train an RL policy on an arbitrary yet cheap machine.

Meaning I want to train a robot (made of pulleys, joints, strings and what have you) to, for instance, go as far as possible without falling.
All this within a simulation that is both Physics-compliant and fast. Just so that later I'd be able to finalize training on the actual [/r/Outside](https://www.reddit.com/r/Outside) robot.

I want my laptop to not die and generally still be usable while this training process runs so it'd be great to run this on some 60 core instance at around $1/hour somewhere.
But bringing the training code and simulator and also copying out the results should be simple.

So check this out from my [CLI tools implemented as `docker build` calls](https://github.com/fenollp/dockerhost-tools)-backpocket:

```shell
export DOCKER_BUILDKIT=1
export DOCKER_HOST=ssh://much.oomphr.dev # A beefy machine
                                         # with many cores
                                         # and much oomph!
# https://oomphr.dev ..love this service! can't wait for it to completely exist

docker build --output=. \
  --build-arg ALGO_NAME=td3 \
  --build-arg ENV_ID=Hopper-v3 \
  https://github.com/fenollp/dockerhost-tools--rl-gym-sb3.git
```

Yes, [you can `docker build` Git repositories](https://docs.docker.com/engine/reference/commandline/build/#git-repositories).
Although BuildKit only recently supports this for git subfolders so I have created a dedicated repo until [moby/buildkit #2116](https://github.com/moby/buildkit/pull/2116) is in [docker-ce](https://docs.docker.com/engine/release-notes/).


This ran on a 6c/*12t* 32GiB amd64 machine for about *5 hours* thanks to this `DOCKER_HOST` environment variable: Docker's ability to execute jobs on another/remote daemon.
It then [downloads the results](./assets/sha256/0cbcc1d1870efdb2cd0fa2e83389397944f1356766ed95af642b950d9a3483e3.zip) to `$PWD`.

Then if you went through the hoops of installing [OpenAI's `gym`](https://gym.openai.com/), [DeepMind's MuJoCo](https://mujoco.org/), [`mujoco_py`](https://github.com/openai/mujoco-py/tree/f1312cceeeebbba17e78d5d77fbffa091eed9a3a#install-and-use-mujoco-py) and to clone this repo https://github.com/DLR-RM/rl-baselines3-zoo, then you should be able to enjoy a trained robot running in its simulated world with:
```shell
python enjoy.py --algo td3 --env Hopper-v3 --folder . --exp-id 0
```

You also get [tensorboard](https://www.tensorflow.org/tensorboard) graphs along with the RL model:
```shell
tensorboard --logdir tensorboard
# ...
# TensorBoard 2.7.0 at http://localhost:6006/ (Press CTRL+C to quit)
```

![](./assets/sha256/5992d8019a923170c32e3dfdd73c0379c7c91539b141824e1e92d4e0dc946ca7.png)
![](./assets/sha256/18a092d0ca8294c9444b830f302bbd838846e76c1ef7bdaa51921ad754265f20.png)
