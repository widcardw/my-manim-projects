import numpy as np


def relu(x):
    return (abs(x) + x) / 2


def linear_step(x, x_min, x_max):
    return np.clip(x, x_min, x_max)
