#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:03:34 2024

@author: pengzhenxian
"""

def BSearch(data, x):
    low = 0
    high = len(data) - 1
    while (low <= high):
        mid = (low + high) // 2
        if(data[mid] == x):
            return mid
        elif (data[mid] < x):
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    data = [int(i) for i in range(10)]
    print(data)
    try:
        x = int(input('输入要查找的数据: '))
    except ValueError:
        print('数据类型错误')
        return
    pos = BSearch(data, x)
    if(pos == -1):
        print('{}不在{}中'.format(x, data))
    else:
        print('{}在{}的第{}个位置'.format(x, data, pos + 1))
        
if __name__ == '__main__': 
    main()
    