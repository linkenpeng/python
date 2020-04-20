#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
多线程测试
Pool 线程池的map()方法接收两个参数，第1个参数是函数名，第2个参数是一个列表
'''

from multiprocessing.dummy import Pool
import requests
import time

from lxml import etree


def query(url):
    return requests.get(url)


def test_xpath():
    start = time.time()
    url_list = []
    for i in range(1):
        url_list.append('https://book.douban.com/')
    pool = Pool(5)
    result = pool.map(query, url_list)
    end = time.time()
    print(f'读取网页耗时：{end - start}')

    html_str = result[0].content.decode()
    print(html_str)

    root = etree.Element("html")

    print(root)

    # info = selector.xpath('')

if __name__ == '__main__':
    test_xpath()