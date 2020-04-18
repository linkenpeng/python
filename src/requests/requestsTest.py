#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
requests测试
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