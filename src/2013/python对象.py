# coding=gb2312
import types

print("type")
print(type(4))
print(type("abcd"))
print(type(type("abcd")))
print(type(0+0j))
print(type(0.0))
print(type([]))
print(type(()))
print(type({}))
print()

print("cmp")
# 3.x已经没有了
print()

print("str,repr")
print(str(2e10))
print(repr([0,5,9,9]))
print()

print("isinstance")
def displayNumType(num):
    print(num), 'is',
    if isinstance(num, (int,float,complex)):
        print('a number of type:',type(num).__name__)
    else:
        print('not a number at all!!')
   

displayNumType(-69)
displayNumType(999999999999999999999)
displayNumType(98.6)
displayNumType(-5.2 + 1.9j)
displayNumType('xxx')
    

    
    
    
    
    