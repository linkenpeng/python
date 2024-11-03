# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import imageio
from scipy import integrate
import numpy as np
from scipy.linalg import solve

im = imageio.imread('../../test_data/money.jpeg')
print(im.dtype)
print(im.shape)

def f(x):
    return x + 1

v, err = integrate.quad(f, 1, 2)
print(v)

A = np.array([[2, 3], [5, 4]])
b = np.array([4, 3])
x = solve(A, b)
print(x)