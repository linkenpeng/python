#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:53:59 2024

@author: pengzhenxian
"""

class EdgeUtil:
    def __init__(self):
        pass
    
    def inputEdge(m, n):
        data = [[0 for i in range(n)] for i in range(m)]
        print(data)
        for i in range(m):
            for j in range(n):
                data[i][j] = int(input('input the data[{}{}]'.format(i, j)))
        print(data)
        return data
    
    def createGraph(n):
        edge = []
        for i in range(n):
            adj = map(int, input('{}的所有邻接点有:'.format(i)).split())
            edge.append(adj)
        return edge