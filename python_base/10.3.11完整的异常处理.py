#!/usr/bin/env python

'''
- BaseException
    |- KeyboardInterrupt
    |- SystemExit
    |- Exception
        |- (all other current built-in exceptions) 所有当前内建异常
'''

try :
    pass
except (IOError,NameError):
    pass
except TypeError as etype:
    pass
except ValueError as evalue:
    pass
else:
    pass
finally:
    pass



