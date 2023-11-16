from stable_baselines3 import PPO
import os
from snakeenv import SnakeEnv
import time


def main(timesteps, iters):
	models_dir = f"training3/models/{int(time.time())}/"
	logdir = f"training3/logs/{int(time.time())}/"

	if not os.path.exists(models_dir):
		os.makedirs(models_dir)

	if not os.path.exists(logdir):
		os.makedirs(logdir)

	env = SnakeEnv()
	env.reset()

	model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=logdir)

	TIMESTEPS = timesteps

	for i in range(1,iters):
		iters += 1
		model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"PPO")
		model.save(f"{models_dir}/{TIMESTEPS*iters}")
	
	env.close()

if __name__ == "__main__":
   timesteps = int(input("Ingrese el número de timesteps: "))
   iters = int(input("Ingrese el número de iteraciones: "))
   main(timesteps, iters)