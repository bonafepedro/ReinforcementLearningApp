import stable_baselines3
import torch
import gymnasium
from stable_baselines3 import PPO, DQN
import os
import time
from snakeenv import SnakeEnv

models_dir = f"training10/models/PPO-{int(time.time())}"
logdir = f"training10/logs/PPO-{int(time.time())}"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)


env = SnakeEnv()
env.reset()

model = PPO("MlpPolicy", env, verbose=1, tensorboard_log=logdir)

TIMESTEPS = 10
for i in range(1,10000):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="PPO")
    model.save(f"{models_dir}/{TIMESTEPS*i}")



env.close()
