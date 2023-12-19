#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 21:40:03 2023

@author: pengzhenxian
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

def draw():
    a = np.arange(0.0, 5.0, 0.02)
    plt.subplot(211)
    plt.plot(a, f(a))
    plt.subplot(2,1,2)
    plt.plot(a, np.cos(2*np.pi*t), 'r--')
    plt.show()
    
    
def d1():
    plt.plot([0,2,4,6,8], [3, 1, 4, 5, 2])
    plt.ylabel("grade")
    # 行,列,选择区域
    plt.subplot(3,2,4)
    # 前两个x轴 ， 后两个y轴
    plt.axis([-1,10,0,6])
    # plt.savefig("test", dpi=600)
    plt.show()
  
def multi():
    a = np.arange(10)
    plt.plot(a,a*1.5,'go-', a,a*2.5,'rx', a,a*3.5,'*', a,a*4.5,'b-.')
    plt.show()
  
def chinese():
    matplotlib.rcParams['font.family'] = 'SimHei'
    plt.plot([3, 1, 4, 5, 2])
    plt.ylabel("数轴（值）")
    # plt.savefig("test", dpi=600)
    plt.show()
      
chinese()














