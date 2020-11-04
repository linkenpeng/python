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

def query(url):
    headers = {
        'User-Agent':'{0}'.format(random.sample(USER_AGENT_LIST, 1)[0]),
        'Cookie':'_lxsdk_cuid=17348c37c03c8-0b28af5ab696d4-31607402-13c680-17348c37c04c8; _lxsdk=17348c37c03c8-0b28af5ab696d4-31607402-13c680-17348c37c04c8; _hc.v=fde59df5-96b8-4189-16ae-d379b611b3c0.1594653638; fspop=test; cy=208; cye=foshan; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1604499765; s_ViewType=10; dplet=033cb8523f079f2b3ac97cb59dc90348; dper=77508b93808b6c954dc0f1f88edbe977bb33bf4e9dc37b48a184fe67a4272f70cd186fb83669e91d1369c0031cbcdcaf255e567c0ff4f9ee4ad6521aa12fc6a915ecb87962e1da6618affc0b5fd063b9b30146c5daac0c8de8670a5910c51adb; ll=7fd06e815b796be3df069dec7836c3df; ua=%E8%80%81M%E5%93%A5; ctu=358c3bab65bdc03610c90ac12957311f187d89097d155d3ce9cfd474d0aea169; uamo=15876505396; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604500153; _lxsdk_s=17593a37650-b0e-d8c-1d8%7C%7C356'
    }
    response = requests.get(url, headers)
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

def test_get_dianping():
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

if __name__ == '__main__':
    test_soup()