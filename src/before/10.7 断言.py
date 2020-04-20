#!/usr/bin/env python

'''
- BaseException
    |- KeyboardInterrupt
    |- SystemExit
    |- Exception
        |- (all other current built-in exceptions) 所有当前内建异常
'''

try :
    assert 1 == 0, 'One does not equal zero silly!'
except AssertionError as args:
    print('%s:%s' % (args.__class__.__name__,args))



