#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

def df():
    d = {'国家': ['中国', '美国', '日本'],
                    '地区': ['亚洲', '北美', '亚洲'],
                    '人口': [13.97, 3.28, 1.26],
                    'GDP': [14.34, 21.43, 5.08],
                    }
    df = pd.DataFrame(d)
    print(df)
    print(df['人口'])
    print(type(df)) # pandas.core.frame.DataFrame

    df = pd.DataFrame(d, index=['a', 'b', 'c'])
    print(df)

    df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})
    print(df2)
    '''
        A          B    C  D      E    F
    0  1.0 2013-01-02  1.0  3   test  foo
    1  1.0 2013-01-02  1.0  3  train  foo
    2  1.0 2013-01-02  1.0  3   test  foo
    3  1.0 2013-01-02  1.0  3  train  foo
    '''

    d = {'x': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'y': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
    df = pd.DataFrame(d)
    print(df)
    '''
        x    y
    a  1.0  1.0
    b  2.0  2.0
    c  3.0  3.0
    d  NaN  4.0
    '''

    # 定义一个字典列表
    data = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4, 'z': 5}]

    # 生成DataFrame对象
    df = pd.DataFrame(data)
    print(df)
    '''
    x  y    z
    0  1  2  NaN
    1  3  4  5.0
    '''

    # 指定索引
    df = pd.DataFrame(data, index=['a', 'b'])
    print(df)
    '''
    x  y    z
    a  1  2  NaN
    b  3  4  5.0
    '''

    s = pd.Series(['a', 'b', 'c', 'd', 'e'])
    df = pd.DataFrame(s)
    print(df)

    # 从字典里生成
    df = pd.DataFrame.from_dict({'国家': ['中国', '美国', '日本'],'人口': [13.97, 3.28, 1.26]})
    # 从列表、元组、ndarray中生成
    df =pd.DataFrame.from_records([('中国', '美国', '日本'), (13.97, 3.28, 1.26)])
    # 列内容为一个字典
    #pd.json_normalize(df.col)
    #df.col.apply(pd.Series)

def s():
    s = pd.Series([14.34, 21.43, 5.08], name='gdp')
    print(s)
    '''
    0    14.34
    1    21.43
    2     5.08
    Name: gdp, dtype: float64
    '''
    print(type(s)) # pandas.core.series.Series

def s2():
    pd.Series(['a', 'b', 'c', 'd', 'e'])
    pd.Series(('a', 'b', 'c', 'd', 'e'))
    
    # 由索引分别为a、b、c、d、e的5个随机浮点数数组组成
    s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    s.index # 查看索引
    s = pd.Series(np.random.randn(5)) # 未指定索引

    d = {'b': 1, 'a': 0, 'c': 2}
    s = pd.Series(d)
    s
    '''
    b    1
    a    0
    c    2
    dtype: int64
    '''

    # 如果指定索引，则会按索引顺序，如有无法与索引对应的值，会产生缺失值
    pd.Series(d, index=['b', 'c', 'd', 'a'])
    '''
    b    1.0
    c    2.0
    d    NaN
    a    0.0
    dtype: float64
    '''

    pd.Series(5.)
    '''
    0    5.0
    dtype: float64
    '''

    # 指定索引
    pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
    '''
    a    5.0
    b    5.0
    c    5.0
    d    5.0
    e    5.0
    dtype: float64
    '''


if __name__ == '__main__': 
    df()