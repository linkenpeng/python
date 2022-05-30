#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
requests测试
requests 可以替代 urllib2,3

Scrapy: 优秀的网络爬虫框架

pyspider: 强大的Web页面爬取系统

Beautiful Soup: HTML和XML的解析库

Re：正则表达式解析和处理功能库

Python-Goose: 提取文章类型web页面的功能库
'''

import requests
import re

def test_get():
    html = requests.get('https://www.huashengju.com')
    html_str = html.content.decode()
    #print(html_str)
    title = re.search('title>(.*?)</', html_str, re.S)
    print(title.group(1))

def test_post():
    data = {'username':'15876505396','passType':'code','passCode':'7964','action':'1'}
    html = requests.post('https://www.huashengju.com/?c=user&a=doLogin', data)
    print(html.content.decode())

if __name__ == '__main__':
    test_get()