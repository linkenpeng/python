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
    # 标准差
    print(np.std(a))
    # 方差
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

def statics():
    np.array([10, 20, 30, 40])[:3] # 支持类似列表的切片
    a = np.array([10, 20, 30, 40])
    b = np.array([1, 2, 3, 4])
    a+b # array([11, 22, 33, 44])（矩阵相加）
    a-1 # array([9, 19, 29, 39])
    4*np.sin(a)

    # 以下是一些数学函数的例子，还支持非常多的数学函数
    a.max() # 40
    a.min() # 10
    a.sum() # 100
    a.std() # 11.180339887498949
    a.all() # True
    a.cumsum() # array([10, 30, 60, 100])
    b.sum(axis=1) # 多维可以指定方向

if __name__ == '__main__': 
    npGradient()










