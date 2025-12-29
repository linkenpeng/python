#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
多线程测试
Pool 线程池的map()方法接收两个参数，第1个参数是函数名，第2个参数是一个列表
'''

from multiprocessing.dummy import Pool
import requests
import time
import threading
import multiprocessing

TIMES = 10

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
    for i in range(TIMES):
        query('https://baidu.com')
    end = time.time()
    print(f'单线程循环访问{TIMES}次百度首页，耗时：{end - start}')
    # 23.3696739

def test_multi_time():
    start = time.time()
    url_list = []
    for i in range(100):
        url_list.append('https://baidu.com')
    pool = Pool(5)
    pool.map(query, url_list)
    end = time.time()
    print(f'5线程访问{TIMES}次百度首页，耗时：{end - start}')
    # 5.06048

def print_numbers():
    for i in range(10):
        print(f'thread1: {i}')

def print_letters():
    for letter in 'abcdef':
        print(f'thread2: {letter}')

def thread_test():
    t1 = threading.Thread(target = print_numbers)
    t2 = threading.Thread(target = print_letters)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def square(x):
    return x * x

def multiprocessing_test():
    with multiprocessing.Pool(processes = 4) as pool:
        result = pool.map(square, range(10))
    print(result)

if __name__ == '__main__':
    #thread_test()
    #multiprocessing_test()
    test_time()
    test_multi_time()