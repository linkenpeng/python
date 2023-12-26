#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 10:52:30 2023

@author: pengzhenxian
"""

import pandas as pd
import numpy as np

def createSeries():

    a = pd.Series([9, 8, 7, 6], index=['a','b','c','d'])
    #print(a)
    
    b = pd.Series(25, index=['a','b','c','d'])
    b.name = 'Series对象'
    b.index.name = 'Index'
    print(b)
    print(b[0])
    print(b['a'])
    print(b[:3])
    print(b.get('f', 100))
    
    c = pd.Series({'a':9,'b':8})
    #print(c)
    
    d = pd.Series({'a':9,'b':8} , index=['a','b','c','d'])
    #print(d)
    
    print(c + d)
    
    e = pd.Series(np.arange(5), index=np.arange(9,4,-1))
    #print(e)
    
    #print(e.index)
    #print(e.values)

class DataFrameOperate(object):
    
    def __init__(self, nm = 'Peter'):
        """constructor"""
        self.name = nm # class instance (data)
        print('Created a DataFrameOperate instance for', nm)
        print(50*'-')
    
    def createDataFrame(self, method = 1):
        if(method == 1):
            return pd.DataFrame(np.arange(15).reshape(3, 5))
        elif(method == 2):
            dt = {'one':pd.Series([9, 8, 7, 6], index=['a','b','c','d']),
                  'two':pd.Series({'a':9,'b':8})}
            b = pd.DataFrame(dt)
            return b
        elif(method == 3):
            c = pd.DataFrame(dt, index=['b','c','d'], columns=['two','three'])
            #print(c)
            return c
        else:
            dl = {'one':[1,2,3,4], 'two':[9,8,7,6]}
            d = pd.DataFrame(dl, index=['a','b','c','d'])
            #print(d)
            #print(d.index)
            #print(d.values)
            return d
        
    def operateDataFrame(self):
       d = self.createDataFrame(5)
       newc = d.columns.insert(2, 'add')
       newd = d.reindex(columns=newc, fill_value=200)
       
       print(d)
       
       nc = d.columns.delete(1)
       ni = d.index.insert(3, 'e')
       nd = d.reindex(index=ni, columns=nc, method='ffill')
       print(nd)
       
       f = d.drop(['a','c'])
       print(f)
       
       print(f.drop('b'))
       print(f.drop('one', axis=1))
       
    def calDataFrame(self):
        a = pd.DataFrame(np.arange(12).reshape(3, 4))
        b = pd.DataFrame(np.arange(20).reshape(4, 5))
        c = pd.Series(np.arange(5))
        d = pd.DataFrame(np.arange(12, 0, -1).reshape(3,4))
        
        '''
        print(a+b)
        print(a*b)
        print(b.add(a, fill_value=100))
        print(a.mul(b, fill_value=0))
        print(c)
        print(c-10)
        print(b)
        print(b-c)
        '''
        print(a)
        print(c)
        #print(a > d)
        #print(a -- d)
        print(a > c)
        print(c > 0)


    
dfo = DataFrameOperate('Myron')
dfo.calDataFrame()







