#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:28:33 2024

@author: pengzhenxian
"""

import multiprocessing as mp
import numpy as np
import time

np.random.RandomState(100)
arr = np.random.randint(0, 100, size=[20000, 5])
data = arr.tolist()

def count_in_data(row, mindata = 4, maxdata = 8):
    count = 0
    for d in row:
        if mindata <= d <= maxdata:
            count += 1
    return count

def cal(data):
    start = time.time()
    
    results = []
    for row in data:
        c = count_in_data(row, 4, 8)
        results.append(c)
    
    end = time.time()
    
    print(results[:10])
    print('cal time:', end - start)
    
    
def cal_multi_apply(data):
    start = time.time()
    
    cpu_count = mp.cpu_count()
    print('cpu_count:', cpu_count)
    pool = mp.Pool(cpu_count)
    # 同步阻塞
    results = [pool.apply(count_in_data, args=(row, 4, 8)) for row in data]
    pool.close()
    
    end = time.time()
    
    print(results[:10])
    print('cal_multi_apply time:', end - start)

def cal_multi_map(data):
    start = time.time()
    
    cpu_count = mp.cpu_count()
    print('cpu_count:', cpu_count)
    pool = mp.Pool(cpu_count)
    # 异步不阻塞
    results = pool.map(count_in_data, [row for row in data])
    pool.close()
    
    end = time.time()
    
    print(results[:10])
    print('cal_multi_map time:', end - start)


if __name__ == '__main__':
    cal(data)
    #cal_multi_apply(data)
    cal_multi_map(data)
    
    
    
    
    
    
    
    
    
    
    
    
    