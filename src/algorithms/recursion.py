#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
递归

@author: pengzhenxian
"""
from inpututil import InputUtil

def factorial(n):
    if (n < 0):
        print('请输入正整数')
        return n
    if (n == 0):
        return 1
    else:
        return n * factorial(n-1)
def hano(n, a, b, c):
    if (n < 1):
        print('圆盘数量错误')
        return
    if (n == 1):
        print('{}:{}->{}'.format(n, a, c))
        return
    hano(n-1, a, c, b)
    print('{}:{}->{}'.format(n, a, c))
    hano(n-1, b, a, c)

def main():
    # n = InputUtil.inputOne(int)
    # fact = factorial(n)
    # print(f'{n}的阶乘是{fact}')
    hano(3, 'a', 'b','c')


if __name__ == '__main__': 
    main()








