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

# 递归实现二分搜索
def BSearchRecursion(data, low, high, x):
    if low <= high:
        mid = (low + high) // 2
        if(data[mid] == x):
            return mid
        elif data[mid] < x:
            return BSearchRecursion(data, low + 1, high, x)
        else:
            return BSearchRecursion(data, low, mid - 1, x)
    return -1

# 圆二分搜索
def circleBSearchMin(data):
    start = 0
    end = len(data) - 1
    if end < 1:
        return 0
    while start <= end:
        if end - start < 2:
            if end == start:
                return start
            elif data[start] > data[end]:
                return end
            else:
                return end
        mid = (start + end) // 2
        if data[start] < data[mid]:
            if data[mid] < data[end]:
                end = mid
            elif data[start] < data[end]:
                end = mid
            else:
                start = mid
        else:
            if data[mid] > data[end]:
                start = mid
            elif data[start] < data[end]:
                start = mid
            else:
                end = mid
    return mid


def main():
    data = [int(i) for i in range(10)]
    print(data)
    try:
        x = int(input('输入要查找的数据: '))
    except ValueError:
        print('数据类型错误')
        return
    # pos = BSearch(data, x)
    # pos = BSearchRecursion(data, 0, len(data)-1, x)
    pos = circleBSearchMin(data)
    if(pos == -1):
        print('{}不在{}中'.format(x, data))
    else:
        #print('{}在{}的第{}个位置'.format(x, data, pos + 1))
        print('{}在{}的第{}个位置'.format(data[pos], data, pos))
        
if __name__ == '__main__': 
    main()
    