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

# 汉诺塔
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

# 绘制英寸标尺 方法1
def draw_interval(length):
    if (length > 0):
        draw_interval(length-1)
        draw_line(length)
        draw_interval(length-1)
    
def draw_line(length, label=''):
    line = '-' * length
    if (label != ''):
        line += ' ' + label
    print(line)

def draw_ruler(num, length):
    draw_line(length, '0')
    for j in range(1, 1 + num):
        draw_interval(length-1)
        draw_line(length, str(j))

# 绘制英寸标尺 方法2
def getrulerseg(seq, length):
    if (length == 2):
        return [1]
    else: 
        seq.extend(getrulerseg([], length-1))
        seq.append(length-1)
        seq.extend(getrulerseg([], length-1))
    return seq

def drawruler(length, nums):
    seq = getrulerseg([], length)
    for i in range(nums):
        print('-' * length, i)
        for j in seq:
            print('-'*j)
    print('-' * length, nums)


def ruler_main():
    num, length = InputUtil.inputTuple(int, '输入英寸和刻度长度: ')
    draw_ruler(num, length)
    drawruler(length, num)

def main():
    # n = InputUtil.inputOne(int)
    # fact = factorial(n)
    # print(f'{n}的阶乘是{fact}')
    hano(3, 'a', 'b','c')


if __name__ == '__main__': 
    ruler_main()








