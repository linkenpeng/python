#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

广度优先搜索（Breadth-First Search, BFS）

Created on Sun Aug 18 09:00:04 2024

@author: pengzhenxian
"""

from edgeutil import EdgeUtil
from inpututil import InputUtil
import queue
import math

def shortPath(data, n, start):
    que = queue.Queue(n)
    que.put(start)
    maxData = math.inf
    minDist = [maxData] * n
    minDist[start] = 0
    
    while que.empty() == False:
        i = que.get()
        for j in range(n):
            if(i != j and data[i][j] > 0 and math.isinf(minDist[j])):
                que.put(j)
                minDist[j] = minDist[i] + 1
                print(j, minDist[j])
    return minDist
    
if __name__ == '__main__': 
    n = InputUtil.inputOne(int)
    data = EdgeUtil.createGraph(n)
    start = InputUtil.inputOne(int)
    minDist = shortPath(data, n, start)
    
    
    
    
    
    
    
    
    
    
    
