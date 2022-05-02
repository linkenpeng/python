# coding=gb2312

print('定义函数')

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

print(fact2(n), s)
print(fact3(n), list)

print(addMe2Me(4.25))
print(addMe2Me(10))
print(addMe2Me('Python'))
print(addMe2Me([-1, 'abc']))

print()
print('函数的默认参数')

def foo(debug = True):
    'determine if in debug mode with default argument'
    if debug:
        print('in debug mode')
    print('done')
    
foo()

print(fact(10, 2))
print(fact(10))
print(fact1(10, 2))



