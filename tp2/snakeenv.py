import stable_baselines3
import torch
import os
from subprocess import Popen, PIPE
from typing import Tuple

import numpy as np
import cv2
import random
import time
from collections import deque

import gymnasium as gym
from gymnasium import spaces

from stable_baselines3 import DQN, PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnRewardThreshold

SNAKE_LEN_GOAL = 30

def collision_with_apple(apple_position, score, num_apples):
    apple_position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
    score += 10**num_apples
    return apple_position, score

def collision_with_boundaries(snake_head):
    if snake_head[0]>=500 or snake_head[0]<0 or snake_head[1]>=500 or snake_head[1]<0 :
        return 1
    else:
        return 0

def collision_with_self(snake_position):
    snake_head = snake_position[0]
    if snake_head in snake_position[1:]:
        return 1
    else:
        return 0
    

class SnakeEnv(gym.Env):
    """Custom Environment that follows gym interface."""

    metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self):
        super(SnakeEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(4)
        # Example for using image as input (channel-first; channel-last also works):
        self.observation_space = spaces.Box(low=500, high=500,
                                            shape=(5+SNAKE_LEN_GOAL,), dtype=np.float32)

    def step(self, action):
        
        self.prev_actions.append(action)
        cv2.imshow('a',self.img)
        cv2.waitKey(1)
        self.img = np.zeros((500,500,3),dtype='uint8')
        # Display Apple
        cv2.rectangle(self.img,(self.apple_position[0],self.apple_position[1]),(self.apple_position[0]+10,self.apple_position[1]+10),(0,0,255),3)
        # Display Snake
        for position in self.snake_position:
            cv2.rectangle(self.img,(position[0],position[1]),(position[0]+10,position[1]+10),(0,255,0),3)
        
        # Takes step after fixed time
        t_end = time.time() + 0.02
        k = -1
        while time.time() < t_end:
            if k == -1:
                k = cv2.waitKey(1)
            else:
                continue
                
        # 0-Left, 1-Right, 3-Up, 2-Down, q-Break
        # a-Left, d-Right, w-Up, s-Down



        # Change the head position based on the button direction
        if action == 1:
            self.snake_head[0] += 10
        elif action == 0:
            self.snake_head[0] -= 10
        elif action == 2:
            self.snake_head[1] += 10
        elif action == 3:
            self.snake_head[1] -= 10

        apple_reward = 0
        num_apples = 1 #partimos de 1 para no hacer e**0
        # Increase Snake length on eating apple
        if self.snake_head == self.apple_position:
            self.apple_position, self.score = collision_with_apple(self.apple_position, self.score, num_apples= num_apples)
            self.snake_position.insert(0,list(self.snake_head))
            apple_reward = 10000
            num_apples +=1

        else:
            self.snake_position.insert(0,list(self.snake_head))
            self.snake_position.pop()
        
        # On collision kill the snake and print the score
        if collision_with_boundaries(self.snake_head) == 1 or collision_with_self(self.snake_position) == 1:
            font = cv2.FONT_HERSHEY_SIMPLEX
            img = np.zeros((500,500,3),dtype='uint8')
            cv2.putText(img,'Your Score is {}'.format(self.score),(140,250), font, 1,(255,255,255),2,cv2.LINE_AA)
            cv2.imshow('a',img)
            self.done = True
            self.truncated = True

        euclidean_dist_to_apple = np.linalg.norm(np.array(self.snake_head) - np.array(self.apple_position))
        self.total_reward = ((250 - euclidean_dist_to_apple) + apple_reward)/100

        print(self.total_reward)
        #self.total_reward = len(self.snake_position) - 3  # default length is 3
        self.reward = self.total_reward - self.prev_reward
        self.prev_reward = self.total_reward

        if self.done:
            self.reward -= 10
#        else: 
#            self.reward = self.score 


        head_x = self.snake_head[0]
        head_y = self.snake_head[1]

        apple_delta_x = head_x - self.apple_position[0]
        apple_delta_y = head_y - self.apple_position[1]

        snake_length = len(self.snake_position)


        self.observation = [head_x, head_y, apple_delta_x, apple_delta_y, snake_length] + list(self.prev_actions)
        self.observation = np.array(self.observation)

        info ={}

        return self.observation, self.total_reward, self.done, self.truncated, info


    def reset(self, seed = None):
        self.done = False
        self.truncated = False
        self.img = np.zeros((500,500,3),dtype='uint8')
        # Initial Snake and Apple position
        self.snake_position = [[250,250],[240,250],[230,250]]
        self.apple_position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.score = 0
        self.reward = 0
        self.prev_reward = 0
        self.prev_button_direction = 1
        self.button_direction = 1
        self.snake_head = [250,250]

        # head_x, head_y, aple_x, aple_y, snake_length, previous_moves
        head_x = self.snake_head[0]
        head_y = self.snake_head[1]

        apple_delta_x = head_x - self.apple_position[0]
        apple_delta_y = head_y - self.apple_position[1]

        snake_length = len(self.snake_position)


        self.prev_actions = deque(maxlen=SNAKE_LEN_GOAL)

        for _ in range(SNAKE_LEN_GOAL):
            self.prev_actions.append(-1)

        self.observation = [head_x, head_y, apple_delta_x, apple_delta_y, snake_length] + list(self.prev_actions)
        self.observation = np.array(self.observation)

        self.info = {} #tratamos de ver de solucionar el error

        return self.observation, self.info