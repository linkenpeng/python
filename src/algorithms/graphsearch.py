#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:00:04 2024

@author: pengzhenxian
"""

# 集合存储邻接点
def edge_by_collection():
    n = 7
    v = init_v(n)
    edge = [{v[1],v[3]},{v[4],v[3]},{v[0],v[5]},{v[2],v[4],v[5],v[6]},{v[6]},{},{v[5]}]
    print_edge(n, v, edge)
    
# 列表存储邻接点
def edge_by_list():
    n = 7
    v = init_v(n)
    edge = [[v[1],v[3]],[v[4],v[3]],[v[0],v[5]],[v[2],v[4],v[5],v[6]],[v[6]],[],[v[5]]]
    print_edge(n, v, edge)

# 字典存储邻接点
def edge_by_dict():
    n = 7
    v = init_v(n)
    edge = [{v[1]:1,v[3]:1},{v[4]:1,v[3]:1},{v[0]:1,v[5]:1},
            {v[2]:1,v[4]:1,v[5]:1,v[6]:1},{v[6]:1},{},{v[5]:1}]
    print(v)
    print(edge)
    print(edge[5])
    print(edge[2][v[5]])
    try:
        print(edge[2][v[3]])
    except KeyError:
        print('{}->{}没有边存在'.format(v[2], v[3]))

# 嵌套字典字典存储邻接点
def edge_by_dict1():
    n = 7
    v = init_v(n)
    edge = {v[0]: {v[1],v[3]}, v[1]:{v[4],v[3]}, v[2]:{v[0],v[5]},
            v[3]:{v[2], v[4], v[5],v[6]}, v[4]:{v[6]}, v[5]:{}, v[6]:{v[5]}}
    print(v)
    print(edge)
    print(edge[v[4]])
    print(v[2] in edge[v[4]])
    print(v[0] in edge[v[2]])

# 嵌套字典存储邻接点（带权）
def edge_by_dict3():
    n = 7
    v = init_v(n)
    edge = {v[0]:{v[1]:1,v[3]:1}, v[1]:{v[4]:1,v[3]:1}, v[2]:{v[0]:1,v[5]:1},
            v[3]:{v[2]:1,v[4]:1,v[5]:1,v[6]:1}, v[4]:{v[6]:1}, v[5]:{}, v[6]:{v[5]:1}}
    print(v)
    print(edge)
    print(edge[v[5]])
    print(edge[v[2]][v[5]])
    try:
       print(edge[v[2]][v[3]])
    except KeyError:
       print('{}->{}没有边存在'.format(v[2], v[3]))
       
# 邻接矩阵存储邻接点
def edge_by_metric():
    n = 7
    v = init_v(n)
    edge = [[0,1,0,1,0,0,0], [0,0,0,1,1,0,0],[1,0,0,0,0,1,0],[0,0,1,0,1,1,1],[0,0,0,0,0,0,1],
            [0,0,0,0,0,0,0],[0,0,0,0,0,0,1]]
    print(v)
    print(edge)
    print(edge[5])
    print(edge[2][3])
    print(edge[2][5])
   

def init_v(n):
    v = ['v' + str(i+1) for i in range(n)]
    return v

def print_edge(n, v, edge):
    print(v)
    print(edge)
    print(edge[2])
    print('v6' in edge[2])
    print(v[5] in edge[2])
    for i in range(n):
        if(v[i] in edge[2]):
            print('v3->v{}'.format(i+1))



if __name__ == '__main__': 
    edge_by_metric()
