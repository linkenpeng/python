# coding=gb2312
import common as cm
import pdb

print('���庯��')

'''
������������
��Python�У�ֻ��ģ�飨module)����(class)���Լ�����(def��lambda)�Ż������µ�������
�����Ĵ���飨��if/elif/else/, for/while��)�ǲ��������µ��������
'''
x = int(2.0) # �ڽ�������
g_count = 0 # ȫ��������
def outer():
    print(x)
    global g_count
    print(g_count)
    o_count = 1 # �հ�������ĺ�����
    g_count = g_count + 1
    print("outer g_count:", g_count)
    print("outer o_count:", o_count)
    def inner():
        i_count = 2 # �ֲ�������
        pdb.set_trace()
        nonlocal o_count # �������ⲿ����ͬ������
        o_count = 10
        print("inner o_count: ", o_count)
        print("inner x: ", x)
        print("inner g_count", g_count)
    inner()
    print("outer o_count:", o_count)


outer()
print("global g_count:", g_count)
print("-" * 30)

def addMe2Me(x):
    'apply + operation to argument'
    return (x + x)

# *b �ɱ����
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
    # ȫ�ֱ���
    global s
    for i in range(1, n + 1):
        s *= i
    return s

list = [1,2]
def fact3(n):
    # ȫ�ֱ���
    list.append(3)
    return list

print(fact2(n), s)
print(fact3(n), list)

print(addMe2Me(4.25))
print(addMe2Me(10))
print(addMe2Me('Python'))
print(addMe2Me([-1, 'abc']))

print()
print('������Ĭ�ϲ���')

def foo(debug = True):
    'determine if in debug mode with default argument'
    if debug:
        print('in debug mode')
    print('done')
    
foo()

print(fact(10, 2))
print(fact(10))
print(fact1(10, 2))

cm.function("a", "b")


