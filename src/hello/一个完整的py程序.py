# coding=utf-8
#/usr/bin/env python (1)起始行

"this is a test module" # (2)模块文档

import sys #(3) 模块导入
import os

debug = True #(4) (全局)变量定义

class FooClass (object): #(5) 类定义(若有)
    "Foo class"
    pass

def test(): #(6)函数定义(若有)
    "test function"
    foo = FooClass()
    
    if debug:
        print('ran test()')
        
if __name__ == '__main__': #(7) 主程序
    test()
