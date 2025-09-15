#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
多线程测试
Pool 线程池的map()方法接收两个参数，第1个参数是函数名，第2个参数是一个列表
'''

from multiprocessing.dummy import Pool
import requests
import time

def cal_power2(num):
    return num * num

def test_multi():
    pool = Pool(3)
    origin_num = [x for x in range(10)]
    result = pool.map(cal_power2, origin_num)
    print(f'计算0-9的平方分别为：{result}')

def query(url):
    requests.get(url)

def test_time():
    start = time.time()
    for i in range(100):
        query('https://baidu.com')
    end = time.time()
    print(f'单线程循环访问100次百度首页，耗时：{end - start}')
    # 23.3696739

def test_multi_time():
    start = time.time()
    url_list = []
    for i in range(100):
        url_list.append('https://baidu.com')
    pool = Pool(5)
    pool.map(query, url_list)
    end = time.time()
    print(f'5线程访问100次百度首页，耗时：{end - start}')
    # 5.06048

if __name__ == '__main__':
    test_time()
    test_multi_time()