#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 21:46:50 2023

@author: pengzhenxian
"""

import numpy as np

def npSum():
    a = np.arange(15).reshape(3,5)
    print(a)
    s = np.sum(a)
    print(s)
    m = np.mean(a, axis=1)
    print(m)
    m1 = np.mean(a, axis=0)
    print(m1)
    avg = np.average(a, axis=0,weights=[10,5,1])
    print(avg)
    print(np.std(a))
    print(np.var(a))

def npMax():
    a = np.arange(15,0,-1).reshape(3,5)
    print(a)
    print(np.max(a))
    print(np.argmax(a))
    print(np.unravel_index(np.argmax(a), a.shape))
    print(np.ptp(a))
    print(np.median(a))

def npGradient():
    a = np.random.randint(0,20,(5))
    print(a)
    print(np.gradient(a))
    b = np.random.randint(0,20,(5))
    print(b)
    print(np.gradient(b))
    c = np.random.randint(0,50,(3,5))
    print(c)
    print(np.gradient(c))


npGradient()












