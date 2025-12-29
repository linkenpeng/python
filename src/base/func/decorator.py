#!/usr/bin/env python
from time import ctime, sleep

def my_decorator(func):
    def wrapper():
        print("do before")
        func()
        print("do after")
    return wrapper

@my_decorator
def say_hello():
    print("hello")

def tsfunc(func):
    def wrappedFunc():
        print('[%s] %s() called'%(ctime(),func.__name__))
        return func()
    return wrappedFunc
    
@tsfunc
def foo():
    pass    
    
def main():
    say_hello()
    foo()
    sleep(4)
    
    for i in range(2):
        sleep(1)
        foo()
         
if __name__ == '__main__':
    main()