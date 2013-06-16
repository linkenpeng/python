# coding=utf-8
#/usr/bin/env python

"斐波那契函数"

from time import sleep, ctime
from myThread import MyThread

def fib(x):
    sleep(0.005)
    if x < 2: return 1
    return (fib(x-2) + fib(x-1))
    
def fac(x):
    sleep(0.1)
    if x < 2: return 1
    return (x * fac(x-1))

def sum(x):
    sleep(0.1)
    if x < 2: return 1
    return (x + sum(x-1))



def singleFunc(nfuncs):
    print('*** SINGLE THREAD')
    for i in nfuncs:
        print('starting ' + funcs[i].__name__ + ' at: ' + ctime())
        print(funcs[i](n))
        print(funcs[i].__name__ + ' finished at: ' + ctime())       

def multiFunc(nfuncs):
    print('\n*** MULTIPLE THREADS')
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)
        
    for i in nfuncs:
        threads[i].start()
            
    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())
        
'''
func: 函数名
tn:   线程个数
'''   
def mFunc(func, tn):
    mThread = []    
    for i in range(tn):
        print('append: ', i)
        t = MyThread(func, (tn,), fib.__name__)
        mThread.append(t)
        
    for i in range(tn):
        print('start:' ,i)
        mThread[i].start()
        
    for i in range(tn):
        print('join: ',i)
        mThread[i].join()     
        print(mThread[i].getResult())


funcs = [fib, fac, sum]
n = 12 
        
def main():
#    nfuncs = range(len(funcs))    
#    singleFunc(nfuncs)    
#    multiFunc(nfuncs)        
     mFunc(fib,10)
#    print('All DONE')
     
if __name__ == '__main__':
    main()
    
    
    

