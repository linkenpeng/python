#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:37:03 2024

@author: pengzhenxian
"""

class InputUtil:
    def __init__(self):
        pass
        
    def inputOne(type_func):
        if (callable(type_func)):
            try:
                x = type_func(input('输入数据: '))
            except ValueError:
                print('数据类型错误, 需要输入: {}'.format(type_func))
                return
        else:
            x = input('输入数据: ')
        return x
    
    def inputList(n, type_func=None):
        if (n <= 0):
            raise ValueError('必须是正整数!')
            return
        result = list()
        for i in range(n):
            if (callable(type_func)):
                try:
                    result.append(type_func(input("输入第{}个数据: ".format(i+1))))
                except ValueError:
                    print('数据类型错误, 需要输入: {}'.format(type_func))
                    return
            else: 
                result.append(input("输入第{}个数据: ".format(i+1)))
        return result

if __name__ == '__main__': 
    print(InputUtil.inputList(3))
    print(InputUtil.inputList(3, int))
    
    
    
    