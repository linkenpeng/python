# coding=gb2312
import common as cm
import pdb

print('定义函数')

'''
变量的作用域
在Python中，只有模块（module)、类(class)、以及函数(def、lambda)才会引入新的作用域
其他的代码块（如if/elif/else/, for/while等)是不会引入新的作用域的
'''
x = int(2.0) # 内建作用域
g_count = 0 # 全局作用域
def outer():
    print(x)
    global g_count
    print(g_count)
    o_count = 1 # 闭包函数外的函数中
    g_count = g_count + 1
    print("outer g_count:", g_count)
    print("outer o_count:", o_count)
    def inner():
        i_count = 2 # 局部作用域
        pdb.set_trace()
        nonlocal o_count # 可以让外部变量同步更新
        o_count = 10
        print("inner o_count: ", o_count)
        print("inner x: ", x)
        print("inner g_count", g_count)
    inner()
    print("outer o_count:", o_count)

'''
outer()
print("global g_count:", g_count)
print("-" * 30)
'''

def addMe2Me(x):
    'apply + operation to argument'
    return (x + x)

# *b 可变参数
def fact(n, *b):
    s = 1
    for i in range(1, n + 1):
        s *= i
    for item in b:
        s *= item
    return s

def fact1(n, m = 1):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s // m

n, s = 10, 100
def fact2(n):
    # 全局变量
    global s
    for i in range(1, n + 1):
        s *= i
    return s

list = [1,2]
def fact3(n):
    # 全局变量
    list.append(3)
    return list

'''
print(fact2(n), s)
print(fact3(n), list)

print(addMe2Me(4.25))
print(addMe2Me(10))
print(addMe2Me('Python'))
print(addMe2Me([-1, 'abc']))

print()
print('函数的默认参数')
'''

def foo(debug = True):
    'determine if in debug mode with default argument'
    if debug:
        print('in debug mode')
    print('done')

'''    
foo()

print(fact(10, 2))
print(fact(10))
print(fact1(10, 2))

cm.function("a", "b")

print(50*'-')
'''

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
    
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword    
    


