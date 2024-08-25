#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:22:58 2024

@author: pengzhenxian
"""
import random as rd
from inpututil import InputUtil
from edgeutil import EdgeUtil
import queue as que

# 用list实现队列
def listQueue(n):
    my_queue = []
    for i in range(n):
        d = rd.randint(0,100)
        print(d, end='')
        my_queue.append(d)
    print('queue pop' + 20 * '-')
    while len(my_queue) > 0:
        d = my_queue.pop(0)
        print(d, end='')
    return

# python自带的队列库,实现队列
def pyQueue(n):
    q = que.Queue(n)
    for i in range(n):
        d = rd.randint(0,100)
        print(d, end='')
        q.put(d)
    print('del queue' + 20 * '-')
    while q.empty() == False:
        d = q.get()
        print(d, end='')
    return

# python自带的队列库,实现栈    
def pyStack(n):
    s = que.LifoQueue(n)
    for i in range(n):
        d = rd.randint(0,100)
        print(d)
        s.put(d)
    print('dequeue' + 20 * '-')
    while s.empty() == False:
        d = s.get()
        print(d)
    return



if __name__ == '__main__': 
    n = InputUtil.inputOne(int)
    pyQueue(n)
    pyStack(n)
    
    
    
    
    
    