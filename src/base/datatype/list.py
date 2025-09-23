#!/usr/bin/env python
#-*- coding:utf8 -*-

def init_list():
    x = [] # 空列表
    x = [1, 2, 3, 4, 5]
    x = ['a', 'b', 'c']
    x = ['a', 1.5, True, [2, 3, 4]] # 各种类型混杂
    type(x) # list 类型检测
def list_op():
    a = [1, 2, 3]
    len(a) # 3（元素个数）
    max(a) # 3（最大值）
    min(a) # 1（最小值）
    sum(a) # 6（求和）
    a.index(2) # 1（指定元素位置）
    a.count(1) # 1（求元素的个数）
    for i in a: print(i) # 迭代元素
    sorted(a) # 返回一个排序的列表，但不改变原列表
    any(a) # True（是否至少有一个元素为真）
    all(a) # True（是否所有元素为真）
    a.append(4) # a: [1, 2, 3, 4]（增加一个元素）
    a.pop() # 每执行一次，删除最后一个元素
    a.extend([9,8]) # a: [1, 2, 3, 9, 8]（与其他列表合并）
    a.insert(1, 'a') # a: [1, 'a', 2, 3]（在指定索引位插入元素，索引从0开始）
    a.remove('a') # 删除第一个指定元素
    a.clear() # []（清空）

# 推导式
def list_infer():
    # 将一个可迭代的对象展开，形成一个列表
    [i for i in range(5)]
    # [0, 1, 2, 3, 4]

    # 可以将结果进行处理
    ['第'+str(i) for i in range(5)]
    # ['第0', '第1', '第2', '第3', '第4']

    # 可以进行条件筛选，实现取偶数
    [i for i in range(5) if i%2==0]

    # 拆开字符，过滤空格，全变成大写
    [i.upper() for i in 'Hello world' if i != ' ']
    # ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']

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






