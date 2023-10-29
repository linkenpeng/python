#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:42:19 2023

@author: pengzhenxian
"""
import numpy as np
  
def saveCSV():    
    a = np.arange(100).reshape((5,20))
    np.savetxt("a.csv", a, fmt='%d', delimiter=',')
 
def readCSV():    
    # .gz .bz2 等都可以
    b = np.loadtxt("a.csv", dtype=np.int32, delimiter=',')
    print(b)
    
def saveFile(bn = True):    
    a = np.arange(100).reshape((5,10,2))
    if(bn): 
        a.tofile("b.bat", format='%d')
    else:
        a.tofile("b.bat", sep=',', format='%d')

def readFile(bn = True):   
    if(bn): 
        b = np.fromfile("b.bat", dtype=np.int32)
    else:
        b = np.fromfile("b.bat", dtype=np.int32, sep=",")
    print(b)
    print(b.reshape(5,10,2))

def npySaveLoad():   
    a = np.arange(100).reshape((5,10,2))
    np.save("a.npy", a)
    b = np.load("a.npy")
    print(b)

    
npySaveLoad()
