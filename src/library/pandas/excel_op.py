#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

https://www.pypandas.cn

Created on Mon Sep 16 09:35:52 2024

@author: pengzhenxian
"""

import pandas as pd

def read():
    source_file = '../../test_data/company.xlsx'
    df = pd.read_excel(source_file)
    print(df.head())
    
    
    targe_file = '../../test_data/company_temp.xlsx'
    df.to_excel(targe_file)
    
def write():
    pass

if __name__ == '__main__': 
    read()