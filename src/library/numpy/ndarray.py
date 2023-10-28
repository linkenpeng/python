# -*- coding: utf-8 -*-

import numpy as np

# A2 + B3 = ?
def pySum():
    a = [0,1,2,3,4]
    b = [9,8,7,6,5]
    c = []
    for i in range(len(a)):
        c.append(a[i] ** 2 + b[i] ** 3)
    return c

def npSum():
    a = np.array([0,1,2,3,4])
    b = np.array([9,8,7,6,5])
    c = a ** 2 + b ** 3
    return c

# ndarray N维数组对象，底层是C语言
'''
ndarray
.ndim 秩 轴的数量或维度的数量
.shape ndarray对象的尺度，对于矩阵,n行m列
.size ndarray对象的个数，相当于.shape中 n*m的值
.dtype ndarray对象的元素类型
.itemsize 每个对象的元素的大小
'''

def ndCreate():
    a = np.array([0,1,2,3])
    print(a)
    
    b = np.array((0,1,2,3))
    print(b)
    
    c = np.array([[1,2],[9,8],[0.1,0.2]])
    print(c)
    
    e = np.arange(10)
    print(e)
    
    f = np.ones((2,3))
    print(f)
    fl = np.ones_like((2,3))
    print(fl)
    
    f1 = np.ones((2,3,4))
    print(f1)
    
    g = np.zeros((2,3), dtype=np.int32)
    print(g)
    g1 = np.zeros_like((2,3))
    print(g1)
    
    h = np.full((2,3),3)
    print(h)
    hf = np.full_like((2,3), 4)
    print(hf)
    
    i = np.eye(3)
    print(i)
    
    j = np.linspace(0, 10, 4, endpoint=False)
    print(j)
    
    k = np.concatenate((a,b))
    print(k)
    
def changeShape():
    a = np.ones((2,3,4), dtype=np.int32)
    print(a)
    a.reshape((3,8))
    print(a)
    a.resize((3,8))
    print(a)
    a.flatten()
    print(a)
    b = a.flatten()
    print(b)
    
def changeType():
    a = np.ones((2,3,4), dtype=np.int32)
    print(a)
    b = a.astype(np.float32)
    print(b)
    
def arr2list():
    a = np.full((2,3,4), 25, dtype=np.int32)
    print(a)
    print(a.tolist())

# 索引和切片
def sliceNp():
    a = np.array([1,2,3,4,5,6])
    print(a[2])
    # 开始,终止（不含），步长
    print(a[1 : 5 : 2])
    
    b = np.arange(24).reshape((2,3,4))
    print(b)
    print(b[1,2,3]) # 23
    print(b[0,1,2]) # 6
    print(b[-1,-2,-3]) # 17
    
    print(b[:,1,3])
    print(b[:,1:3,:])
    print(b[:,:,::2])
    
# 运算    
def calNp():    
    a = np.arange(24).reshape((2,3,4))
    print(a.mean())
    a = a / a.mean()
    print(a)
    
    b = np.arange(24).reshape((2,3,4))
    c = np.sqrt(b)
    print(np.square(b))
    print(np.maximum(a,b))
    print(np.modf(b))
    print(b > c)
    
calNp()













