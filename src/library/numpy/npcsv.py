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
    
readCSV()
