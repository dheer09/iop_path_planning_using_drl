import numpy as np
from math import atan2

from publisher_subscriber import *

# actions: 0 = forward, 1 = backward, 2 = left, 3 = right

def calc_dist(curr_state, target_state):
    # numpy arrays
    point1 = np.array((curr_state[0], curr_state[1]))
    point2 = np.array((target_state[0], target_state[1]))
 
    # calculating Euclidean distance
    # using linalg.norm()
    dist = np.linalg.norm(point1 - point2)
    return dist

def calc_target_angle(curr_state, target_state):
    inc_x = target_state[0] - curr_state[0]
    inc_y = target_state[1] - curr_state[1]

    target_angle = atan2(inc_y, inc_x)
    return target_angle

def calc_reward(dist, time, target_angle):
    reward = 0
    target_angle = 0
    reward = -(dist**2 + (time/1000) + target_angle**2)
    return reward


def step(curr_state, action, target_state, time):
    
    reward = -1 # TODO
    dist = calc_dist(curr_state, target_state)
    epsilon = 0.005
    done = False
    next_state = None
    if(dist < epsilon):
        next_state = target_state
        done = True
        reward = 100 # TODO
        return (next_state, reward, done)
    
    target_angle = calc_target_angle(curr_state, target_state)
    reward = calc_reward(dist, time, target_angle)
    publish_action(action)

    next_state = calc_next_state()
    return (next_state, reward, done)
