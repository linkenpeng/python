#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import time

def read_csv(file_path):
    # 文件目录
    pd.read_csv('data.csv') # 如果文件与代码文件在同一目录下
    pd.read_csv('data/my/data.csv') # 指定目录
    pd.read_csv('data/my/my.data') # CSV文件的扩展名不一定是.csv

    # 使用URL
    df = pd.read_csv('https://www.gairuo.com/file/data/dataset/GDP-China.csv')
    print(df.head())

def read_io():
    from io import StringIO
    data = ('col1,col2,col3\n'
            'a,b,1\n'
            'a,b,2\n'
            'c,d,3')

    pd.read_csv(StringIO(data))
    df = pd.read_csv(StringIO(data), dtype=object)   
    print(df.head())
     # 数据分隔符默认是逗号，可以指定为其他符号
    pd.read_csv(data, sep='\t') # 制表符分隔tab
    pd.read_table(data) # read_table 默认是制表符分隔tab
    pd.read_csv(data, sep='|') # 制表符分隔tab
    pd.read_csv(data,sep="(?<!a)\|(?!1)", engine='python') # 使用正则表达式

    pd.read_csv(data, header=0) # 第一行
    pd.read_csv(data, header=None) # 没有表头
    pd.read_csv(data, header=[0,1,3]) # 多层索引MultiIndex

    pd.read_csv(data, names=['列1', '列2']) # 指定列名列表
    pd.read_csv(data, names=['列1', '列2'], header=None)

    # 支持int、str、int序列、str序列、False，默认为None
    pd.read_csv(data, index_col=False) # 不再使用首列作为索引
    pd.read_csv(data, index_col=0) # 第几列是索引
    pd.read_csv(data, index_col='年份') # 指定列名
    pd.read_csv(data, index_col=['a','b']) # 多个索引
    pd.read_csv(data, index_col=[0, 3]) # 按列索引指定多个索引

    # 支持类似列表的序列和可调用对象
    # 读取部分列
    pd.read_csv(data, usecols=[0,4,3]) # 按索引只读取指定列，与顺序无关
    pd.read_csv(data, usecols=['列1', '列5']) # 按列名，列名必须存在
    # 指定列顺序，其实是df的筛选功能
    pd.read_csv(data, usecols=['列1', '列5'])[['列5', '列1']]
    # 以下用callable方式可以巧妙指定顺序，in后面的是我们要的顺序
    pd.read_csv(data, usecols=lambda x: x.upper() in ['COL3', 'COL1'])

    # 布尔型，默认为False
    # 下例只取一列，会返回一个Series
    pd.read_csv(data, usecols=[0], squeeze=True)
    # 有两列则还是df
    pd.read_csv(data, usecols=[0, 2], squeeze=True)

    # 格式为字符型str
    # 表头为c_0、c_2
    pd.read_csv(data, prefix='c_', header=None)

    # 布尔型，默认为True
    data = 'a,b,a\n0,1,2\n3,4,5'
    pd.read_csv(StringIO(data), mangle_dupe_cols=True)
    # 表头为a b a.1
    # False会报ValueError错误

    # 传入类型名称，或者以列名为键、以指定类型为值的字典
    pd.read_csv(data, dtype=np.float64) # 所有数据均为此数据类型
    pd.read_csv(data, dtype={'c1':np.float64, 'c2': str}) # 指定字段的类型
    
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    pd.read_csv(data, dtype=[datetime, datetime, str, float]) # 依次指定

    # 格式为engine=None，其中可选值有{'c', 'python'}
    pd.read_csv(data, engine='c')

def read_bytes_io():
    from io import BytesIO
    data = (b'word,length\n'
            b'Tr\xc3\xa4umen,7\n'
            b'Gr\xc3\xbc\xc3\x9fe,5')

    df = pd.read_csv(BytesIO(data))
    print(df.head())

def write_file(file_path, data):
    pd.to_csv(file_path, data)

if __name__ == '__main__': 
    read_io()