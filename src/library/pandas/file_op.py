#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

def read_excel(file_path):
    # 返回DataFrame
    pd.read_excel('team.xlsx') # 默认读取第一个标签页Sheet
    pd.read_excel('path_to_file.xlsx', sheet_name='Sheet1') # 指定Sheet
    # 从URL读取
    pd.read_excel('https://www.gairuo.com/file/data/dataset/team.xlsx')

def read_json():
    # data.json为同目录下的一个文件
    pd.read_json('data.json')

def read_html():
    url = 'https://www.gairuo.com/p/pandas-io'
    dfs = pd.read_html(url)
    dfs[0] # 查看第一个df
    # 读取网页文件，第一行为表头
    dfs = pd.read_html('data.html', header=0)
    # 第一列为索引
    dfs = pd.read_html(url, index_col=0)
    # id='table'的表格，注意这里仍然可能返回多个
    dfs1 = pd.read_html(url, attrs={'id': 'table'})
    # dfs1[0]
    # class='sortable'
    dfs2 = pd.read_html(url, attrs={'class': 'sortable'})

def read_clipboard():
    '''
    x y z
    a 1 2 3
    b 4 5 6
    c 7 8 9
    '''

    # 复制上边的数据，然后直接赋值
    cdf = pd.read_clipboard()
    print(cdf.head())

def read_sql():
    # 需要安装SQLAlchemy库
    from sqlalchemy import create_engine
    # 创建数据库对象，SQLite内存模式
    engine = create_engine('sqlite:///:memory:')
    # 取出表名为data的表数据
    with engine.connect() as conn, conn.begin():
        data = pd.read_sql_table('data', conn)

    # data
    # 将数据写入
    data.to_sql('data', engine)
    # 大量写入
    data.to_sql('data_chunked', engine, chunksize=1000)
    # 使用SQL查询
    pd.read_sql_query('SELECT * FROM data', engine)


def write_file(file_path, data):
    pd.to_csv(file_path, data)

if __name__ == '__main__': 
    read_sql()