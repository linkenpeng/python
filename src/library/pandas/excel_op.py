#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

https://www.pypandas.cn

Created on Mon Sep 16 09:35:52 2024

@author: pengzhenxian
"""

import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def read():
    source_file = 'test_data/company.xlsx'
    df = pd.read_excel(source_file)
    print(df.head())
    
    
    targe_file = 'test_data/company_temp.xlsx'
    df.to_excel(targe_file)

def read_from_url():
    # 以下两种效果一样，如果是网址，它会自动将数据下载到内存
    df = pd.read_excel('https://www.gairuo.com/file/data/dataset/team.xlsx')
    # df = pd.read_excel('team.xlsx') # 文件在notebook文件同一目录下
    # 如果是CSV，使用pd.read_csv()，还支持很多类型的数据读取
    #print(df.head)
    #print(df.tail)
    #print(df.sample)
    df.shape # (100, 6) 查看行数和列数
    df.info() # 查看索引、数据类型和内存信息
    df.describe() # 查看数值型列的汇总统计
    df.dtypes # 查看各字段类型
    df.axes # 显示数据行和列名
    df.columns # 列名
    
def write():
    pass

if __name__ == '__main__': 
    read()