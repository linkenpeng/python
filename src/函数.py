# coding=gb2312

print('���庯��')

def addMe2Me(x):
    'apply + operation to argument'
    return (x + x)

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




