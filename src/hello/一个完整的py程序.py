# coding=gb2312
#/usr/bin/env python (1)��ʼ��

"this is a test module" # (2)ģ���ĵ�

import sys #(3) ģ�鵼��
import os

debug = True #(4) (ȫ��)��������

class FooClass (object): #(5) �ඨ��(����)
    "Foo class"
    pass

def test(): #(6)��������(����)
    "test function"
    foo = FooClass()
    
    if debug:
        print('ran test()')
        
if __name__ == '__main__': #(7) ������
    test()
