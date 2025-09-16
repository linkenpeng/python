#!/usr/bin/env python
#-*- coding:utf8 -*-

def test():
    print("切片操作,第三个参数代表步长")
    s = 'abcdefgh'
    print(s[::-1]) #可以视作“翻转”操作
    print(s[::2])   #隔一个取一个

    print("range(a,b,c) 返回a-b步长c的列表不包含b")
    for i in range(-1, -len(s), -1):
        print(i,s[:i])
        
    hi = '''
    hi
    there
        '''

    print(repr(hi))
    print(hi)

    print(id(hi))

if __name__ == "__main__":
    test()