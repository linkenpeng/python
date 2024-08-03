#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 09:40:41 2024

@author: pengzhenxian
"""

def init_arr():
    # scores = list(map(float, input('输入考试成绩').split()))
    # print(scores)
    # print('输入补考成绩')
    # for i in range(len(scores)):
    #     if(scores[i] < 60):
    #         scores[i] = float(input('input {}th score:').format(i+1))
    # print(scores)
    
    # init list
    # scores = 30*[0]
    scores = list()
    scores.append(88)
    # scores[0] = 88
    # scores[1] = 67
    print(scores[0])


def init_name():
    names = input('input all names:').split()
    print(names)
    
    n = 3
    names3 = []
    for i in range(n):
        name = input('输入姓名:')
        names3 +=[name]
    print(names3)

class sportname:
    def __init__(self, name='', score=0):
        self._name = name
        self._score = score
        
    def getName(self):
        return self._name
    
    def getScore(self):
        return self._score
    
    def setScore(self, score):
        self._score = score
        
    def prints(self):
        print(self._name, self._score)


def initSportsMan(n):
    if (n <= 0):
        raise ValueError('人数必须是正整数, 请重新运行程序输入人数!')
        return
    sportsman = []
    for i in range(n):
        name, score = input("输入第{}个人的姓名和成绩: ").format(i+1).split()
        sportsman.append(sportname(name, score))
    return sportsman



def printMan(sportsman_list):
    for i in sportsman_list:
        i.prints()

def maxNames(mans, k):
    firstK = k * [0]
    for i in range(k):
        firstK[i] = i
        for j in range(i + 1, len(mans)):
            if(mans[firstK[i]].getScore() < mans[j].getScore()):
                firstK[i] = j
        if (firstK[i] != i):
            mans[firstK[i]], mans[i] = mans[i], mans[firstK[i]]
    return mans

def maxNames2(mans, k):
    firstK = k * [0]
    newmans = sorted(mans, key=lambda sportname:sportname._score, reverse=True)
    firstK = newmans[:k]
    return firstK


def main1():
    try:
        n = int(input('输入人数:'))
    except ValueError:
        print('人数必须是正整数, 请重新输入！')
        return
    try:
        mans = initSportsMan(n)
        printMan(mans)
    except ValueError as e:
        print(e)
        return
    
    k = int(input('需要显示前几名的信息?'))
    if(k <=0 or k > n):
        print('{}不在1...{}范围之间'.format(k, n))
        return
    # sorted_mans = maxNames(mans, k)
    sorted_mans = maxNames2(mans, k)
    print('sorted:')
    printMan(sorted_mans)


if __name__ == '__main__': 
    main1()








