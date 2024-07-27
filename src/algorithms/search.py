#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
穷举搜索

Created on Sat Jul 27 21:37:27 2024

@author: pengzhenxian
"""
import re

def search_by_list(data, x):
    listdata = [1,2,3,4,5,6]
    x = 3
    if(x in listdata):
        print('1:', x, 'is in data')
    else:
        print('1:{} is not in list'.format(x))
    
    c = listdata.count(x)
    if(c > 0):
        print('2:', x, 'is in data')
    else:
        print('2:{} is not in list'.format(x))
    
    try:    
        i = listdata.index(x)
    except ValueError:
        print('3:{} is not in list'.format(x))
    else:    
        if(i >= 0 and i < len(listdata)):
            print('3:', x, 'is in data')

def search1(data, x):
    for y in data:
        if y == x:
            return x
    return -1

def search2(data, x):
    n = len(data)
    for j in range(n):
        if(data[j] == x):
            return j
    return -1

def search_str():
    listdata = 'hello,everynone!hello,mum.hello,daddy!'
    x = 'hello'
    print(re.findall(x, listdata))
    
    comp = re.compile(x)
    y = re.search(comp, listdata).group()
    print(y)

def main():
    data = [1,2,3,4,5]
    x = int(input('输入待查找的整数: '))
    r1 = search1(data, x)
    r2 = search2(data, x)
    if(r1 == -1 or r2 == -1):
        print('{} is not in {}中'.format(x, data))
    else:
        print('{} is in {}中'.format(x, data))
        
if __name__ == '__main__': 
    search_str()









