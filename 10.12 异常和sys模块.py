#!/usr/bin/env python
# coding=utf-8

'''
- BaseException
    |- KeyboardInterrupt
    |- SystemExit
    |- Exception
        |- (all other current built-in exceptions) 所有当前内建异常
'''

try :
    float('abc123')
except:
    import sys
    exc_tuple = sys.exc_info()
    print(exc_tuple)
    for eachItem in exc_tuple:
        print(eachItem)



