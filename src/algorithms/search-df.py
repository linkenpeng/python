#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
深度优先搜索

Created on Sat Aug 31 09:23:37 2024

@author: pengzhenxian
"""

import queue
from edgeutil import EdgeUtil
from inpututil import InputUtil

class Graph:
    def __init__(self, n, name, edges):
        self._n = n
        self._name = name
        self._edges = edges
    
    def setName(self, name):
        self._name = name
    
    def setEdges(self, edges):
        self._edges = edges
    
    def getVexNum(self):
        return self._n
    
    def getVexNames(self):
        return self._name
    
    def getEdge(self):
        return self._edges
    
    def setOneVexName(self, pos, name):
        self._name[pos] = name
    
    def setOneEdge(self, start, end, edge):
        self._edges[start][end] = edge

# 深度优先遍历    
def DSTGraphNoRe(g, i, visit):
    n = g.getVexNum()
    edges = g.getEdge()
    q = queue.LifoQueue(n)
    q.put(i)
    while (q.empty() == False):
        i = q.get()
        for k in range(n):
            if (edges[i][k] == 1 and visit[k] == -1):
                visit[k] = i
                q.put(i)
                q.put(k)
                print('{}->{}'.format(i, k))
                break
    
def DSTNoRe(g):
    n = g.getVexNum()
    visit = [-1 for i in range(n)]
    for k in range(n):
        if(visit[k] == -1):
            visit[k] = 1
            print('init vex:', k)
            DSTGraphNoRe(g, k, visit)
          
''' 递归实现深度优先遍历 '''
def DSTGraph(g, i, visit):
    n = g.getVexNum()
    edges = g.getEdge()
    for k in range(n):
        if (edges[i][k] == 1 and visit[k] == -1):
            visit[k] = i
            print('{}->{}'.format(i, k))
            DSTGraph(g, i, visit)

def DST(g):
    n = g.getVexNum()
    visit = [-1 for i in range(n)]
    
    for k in range(n):
        if(visit[k] == -1):
            visit[k] = 1
            print('init vex:', k)
            DSTGraph(g, k, visit)
    
''' 广度优先遍历 '''    
def BSTGraph(g, i, visit):
    n = g.getVexNum()
    edges = g.getEdge()
    q = queue.Queue(n) # 队列
    q.put(i)
    
    while (q.empty() == False):
        i = q.get()
        print(i)
        for k in range(n):
            if (edges[i][k] == 1 and visit[k] == -1):
                visit[k] = i
                q.put(k)
                print('{}->{}'.format(i, k))
                break
    
def BST(g):
    n = g.getVexNum()
    visit = [-1 for i in range(n)]
    
    for k in range(n):
        if(visit[k] == -1):
            visit[k] = 1
            print('init vex:', k)
            BSTGraph(g, k, visit)
    
    
def inputGraph():
    n = InputUtil.inputOne(int) 
    name = list()
    edges = [[i for i in range(n)] for j in range(n)]
    for i in range(n):
        aname = input('vex {} name:'.format(i))
        name.append(aname)
    for i in range(n):
        for j in range(n):
            e = int(input('edage: {} -> {}'.format(i, j)))
            edges[i][j] = e
    return (n, name, edges)
    
    
    
    
    
    
    
    
    
    