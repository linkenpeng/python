#!/usr/bin/env python
#-*- coding:utf8 -*-

def listTest():
    ls = ["cat", "dog", "tiger", 1024]
    ls2 = [9, 8]
    print(ls)

    # 只是赋值，同一个地址
    lt = ls
    lt.append("jak")

    print(ls)

    ls[1] = "chicken"
    print(ls)

    ls[0:1:1] = "aa"
    print(ls)

    del ls[0:1:1]
    print(ls)

    print(ls + ls2)
    print(ls2 * 2)

    print(ls2.append(7))
    print(ls2.clear())
    print(ls.copy())
    print(ls.insert(0, 99))
    print(ls.pop(0))
    print(ls.remove(1024))
    print(ls.reverse())
    print(ls.index("dog"))

def joinStore():
    ls = ["8163","8222","4193"]
    message = ""
    for store_no in ls:
        message += ' message: "\\\"store_no\\\":\\\"'+store_no+'\\\"" OR'

    print(message)

def test():
    print("列表")
    aList = [1, 2, 3, 4]
    print(aList)
    print(aList[0])
    print(aList[2:])
    print(aList[:3])
    aList[1] = 5
    print(aList)
    print('-' * 30)

    print('元组')
    aTuple = ('robots', 77, 93, 'try')
    print(aTuple)
    print(aTuple[:3])
    # 元组不可修改 aTuple[1] = 5 
    # TypeError: 'tuple' object does not support item assignment
    print('-' * 30)

    print('字典')
    aDict = {'host': 'earth'}
    aDict['port'] = 80
    print(aDict)
    print(aDict.keys())
    print(aDict['host'])
    print('遍历字典')
    for key in aDict:
        print(key, aDict[key])

def test2():

    x = [1, 2, 3, 3, 'a', 3, True]
    s = [1, 2, 3]

    print(s in x)
    print(s not in x)
    print(s + x)
    print(s*2)
    print(s[1])
    # 切片 步长2
    print(x[1:4:2])
    # 从后往前
    print(x[::-1])
    print(len(x))

    print(min(s))
    print(max(s))

    print(s.index(2))
    print(x.index(3, 2, 6))

    print(x.count(3))

if __name__ == '__main__':
    start = joinStore()






