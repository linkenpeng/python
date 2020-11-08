#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
多线程测试
Pool 线程池的map()方法接收两个参数，第1个参数是函数名，第2个参数是一个列表

Python 中 xpath 语法 与 lxml 库解析 HTML/XML 和 CSS Selector
@link https://blog.csdn.net/freeking101/article/details/64461574

XPath 常用规则
表达式	描述
nodename	选取此节点的所有子节点
/	从当前节点选取直接子节点
//	从当前节点选取子孙节点
.	选取当前节点
..	选取当前节点的父节点
@	选取属性
*	通配符，选择所有元素节点与元素名
@*	选取所有属性
[@attrib]	选取具有给定属性的所有元素
[@attrib='value']	选取给定属性具有给定值的所有元素
[tag]	选取所有具有指定元素的直接子节点
[tag='text']	选取所有具有指定元素并且文本内容是text节点


XPath是一门查询语言，它由C语言开发而来，因此速度非常快。
Beautiful Soup4是一个从网页中提取数据的工具，它入门很容易，功能很强大，但是由于是基于Python开发的，因此速度比XPath要慢。

'''

from multiprocessing.dummy import Pool
import requests
import time
import re
import json
import random
from bs4 import BeautifulSoup

from lxml import etree

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"
]

cookies = {
    'huashengju': 'MEIQIA_TRACK_ID=1dS6pSPhWfyVBCY2eTKnjXLlBTK; huashengju_login_name=15876505396; kanbanGuider=kanban-guide; PHPSESSID=d3juc14t72jn858sbmcqnb3hem; huashengju_auth=9104D8KMy2m2gJQFN8oHLOlfSP9q9VVEHi0%2FUvlg3N8Ty4WYxIuHa8t%2FNtYnPLjEOomflinoUkMdz%2F%2B%2F4X7YCFlVefpZ%2F0I; Hm_lvt_f8aa0298cc7d1c9ec6b2b1195f234ed8=1604761056; MEIQIA_VISIT_ID=1k0W4d1e9Qor8FxMGHAtEjiLxV2; huashengju_user_auth=a368HcJ6ORDrEOrqs%2F0wFOP8e7IkeX43saZca8ZYdKRtMB0HINA%2BEUXHsOcYnbOPpeaoZROP%2BQaHv5ZUX8Opt2Rt4LjWTd5N%2By3JJYM; Hm_lpvt_f8aa0298cc7d1c9ec6b2b1195f234ed8=1604839989',
    'zhihu': ''
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,sq;q=0.7,zh-TW;q=0.6',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    #'DNT':'1',
    'Upgrade-Insecure-Requests':'1',
    'Host':'www.huashengju.com',
    'Referer':'https://www.huashengju.com/user-login.html',
    'User-Agent':'{0}'.format(random.sample(USER_AGENT_LIST, 1)[0]),
    'Cookie':cookies['huashengju']
}

def query(url):
    response = requests.get(url, headers = headers)
    html_str = response.content.decode('utf-8')
    return html_str

def get_html(url):
    start = time.time()
    url_list = []
    for i in range(1):
        url_list.append(url)
    pool = Pool(5)
    result = pool.map(query, url_list)
    end = time.time()
    print(f'读取网页耗时：{end - start}')
    return result[0];

def test_xpath():
    start = time.time()
    html_str = get_html('https://www.huashengju.com/')
    #print(html_str)

    selector = etree.HTML(html_str)

    # 提取 li 中的有效信息123
    content = selector.xpath('//div[@id="Subject"]/div/div/a/img/@src')
    img_src_list = []
    for each in content:
        img_src_list.append(each)

    print(img_src_list)

    end = time.time()
    print(f'lxml解析网页耗时：{end - start}')


def test_soup():
    start = time.time()

    html_str = get_html('https://www.huashengju.com/')
    soup = BeautifulSoup(html_str, 'html.parser')
    # title = soup.title
    # print(title)

    imgs = soup.find(id='Subject').find_all('img')
    img_src_list = []
    for x in imgs:
        link = x.get('src')
        if link:
            img_src_list.append(link)
    print(img_src_list)

    end = time.time()
    print(f'soup解析网页耗时：{end - start}')

def get_dianping():
    html_str = get_html('http://www.dianping.com/shop/EZcDMs9sSDQy7PeF')
    print(html_str)
    selector = etree.HTML(html_str)
    content = selector.xpath('//div[@id="basic-info"]/h1/text()')
    for each in content:
        print(each)

def get_content():
    html_str = get_html('http://www.sundxs.com/mingyanyulu/9410.html')
    selector = etree.HTML(html_str)
    content = selector.xpath('//div[@class="content"]/p/text()')

    content_list = []
    f = open('content.txt','w')
    i = 6
    for each in content:
        c = (re.sub('\d+[、.]','', each.strip()))
        if c != '':
            item = {}
            item['id'] = i
            item['note'] = c
            content_list.append(item)
            f.writelines(c + '\n')
            i += 1
    f.close()

    str_json=json.dumps(content_list,indent=2, ensure_ascii=False)
    with open('content.json','w') as f:
        f.write(str_json)

def get_zhihu():
    html_str = get_html('https://www.zhihu.com/')
    print(html_str)
    selector = etree.HTML(html_str)
    content = selector.xpath('//h2[@id="HotItem-title"]/text()')
    for each in content:
        print(each)

def test_cookie():
    session = requests.session()
    html_str = session.get('https://www.huashengju.com/designer-init.html', headers=headers, verify=False)
    print(html_str.content.decode())

if __name__ == '__main__':
    test_cookie()