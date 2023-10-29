#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 21:26:07 2023

@author: pengzhenxian
"""

import numpy as np

def npRandom():
    a = np.random.rand(3, 4, 5)
    print(a)
    sn = np.random.randn(3, 4, 5)
    print(sn)
    np.random.seed(10)
    b = np.random.randint(100, 200, (3,4))
    print(b)
    np.random.seed(10)
    c = np.random.randint(100, 200, (3,4))
    print(c)

def npShuffle():
    a = np.random.randint(100, 200, (3,4))
    print(a)
    np.random.shuffle(a)
    print(a)
    np.random.shuffle(a)
    print(a)

def npPermutation():
    a = np.random.randint(100, 200, (3,4))
    print(a)
    b = np.random.permutation(a)
    print(b)
    print(a)

def npChoice():
    a = np.random.randint(100, 200, (8,))
    print(a)
    b = np.random.choice(a, (3,2),replace=False)
    print(b)

def npUniform():
    u = np.random.uniform(0,10,(3,4))
    print(u)
    n = np.random.normal(10,5,(3,4))
    print(n)
    
npUniform()













