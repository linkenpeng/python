#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
pip install requests
pip install fake_useragent

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
from fake_useragent import UserAgent
ua = UserAgent()

headers = {
 "User-Agent": ua.random
}

print(headers)

def getDongfang(stock_num):
    url = 'https://data.eastmoney.com/zjlx/' + stock_num + '.html'
    html = requests.get(url, headers=headers)
    html_str = html.content.decode()
    #print(html_str)
    title = re.search('title>(.*?)</', html_str, re.S)
    print(title.group(1))

def getDoc():
    url = 'http://www.360doc.com/content/23/1115/09/61825250_1104087237.shtml'
    html = requests.get(url, headers=headers)
    html_str = html.content.decode()
    print(html_str)

def test_get():
    html = requests.get('https://www.huashengju.com', headers=headers)
    html_str = html.content.decode()
    #print(html_str)
    title = re.search('title>(.*?)</', html_str, re.S)
    print(title.group(1))

def test_post():
    data = {'username':'15876505396','passType':'code','passCode':'7964','action':'1'}
    html = requests.post('https://www.huashengju.com/?c=user&a=doLogin', data, headers=headers)
    print(html.content.decode())

if __name__ == '__main__':
    getDoc()