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
    'zhihu': 'SESSIONID=xLmUJpnl3kLk5D30AxvOkBxIz29aWOy5iGDHE1WIttB; JOID=UFgRB0zk6VD1BDmGKeJejJtbKAU-rdszkmV4tECphDOcYF3TfvpyJ6wDP4Iq3QYbmf-waz0SoUUERHZtx7pBPxA=; osd=UlwQBkjm7VH0ADuCKONajp9aKQE8qdoylmd8tUGthjedYVnRevtzI64HPoMu3wIamPuybzwTpUcARXdpxb5APhQ=; _zap=42fdad9c-a310-43c5-8370-2e9b1f079a20; _xsrf=ootmIcwMCYzgNft0OHLWUmCalRaCVRC8; _ga=GA1.2.1579697943.1593702277; d_c0="AIARxVsXhBGPTms_zc_u5N3Kc4ckS27v_NI=|1593702269"; q_c1=9671e446846d4da793b2e43a00063975|1596255608000|1596255608000; l_n_c=1; n_c=1; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1603117855,1604066342,1604195380,1604675463; tshl=; tst=h; SESSIONID=LFd6MnNqakKanwpWRAFON1UrfNSwuOgjDanz2foyvcj; JOID=UF4QBU_HOdjoiwFoHMOLBYLWEu4Kj3y_3MBrJW6gVpCK53AcSN-Bf7OJBmgdeFpyWqLOQEMThm3PLYLy9MxMBsg=; osd=U1wXA0zEO9_uiAJqG8WIBoDRFO0JjXu538NpImijVZKN4XMfStiHfLCLAW4ee1h1XKHNQkQVhW7NKoTx985LAMs=; capsion_ticket="2|1:0|10:1604843253|14:capsion_ticket|44:NzZiZDI4NTAwZTUyNDFkNDkzYzY4MDEzNzZhODY3Y2E=|970d647506311e9ed652b31250fd9e17872159adef924916db51e460fefcb65e"; r_cap_id="ZjViZTQzNGNkMGYzNDlkZDhkMTFjZmE0ZGMwNzE2YTE=|1604843255|1970b5a93d20c0ccabbbb1ece5835537eaef2263"; cap_id="ZGVmNzkxODgwZGQ3NDE1N2I0ODNhMGI4YmVjYTM5MGE=|1604843255|fb8b35d318ed85fdc7a8b3fdf9bcce05e5a84e4e"; l_cap_id="NzJlZmVlYTQxMmVlNDViM2E4NWVmYmQyYzU1MjNhZWM=|1604843255|f6a81b57a0b2bed35401899ffa059e4cdcf900be"; z_c0=Mi4xWDNpYUNBQUFBQUFBZ0JIRld4ZUVFUmNBQUFCaEFsVk5Ga1dWWUFDcXVZVnJvSkRTekxpRW9nT2dTSTh5Q0NxWWhn|1604843286|13a8c12ff2f6ad466e5fd67f36c2f7de7e7c1ed2; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1604843642; KLBRSID=d6f775bb0765885473b0cba3a5fa9c12|1604843360|1604843205',
    'dianping': '_lxsdk_cuid=17348c37c03c8-0b28af5ab696d4-31607402-13c680-17348c37c04c8; _lxsdk=17348c37c03c8-0b28af5ab696d4-31607402-13c680-17348c37c04c8; _hc.v=fde59df5-96b8-4189-16ae-d379b611b3c0.1594653638; fspop=test; cy=208; cye=foshan; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1604499765; s_ViewType=10; ll=7fd06e815b796be3df069dec7836c3df; ua=%E8%80%81M%E5%93%A5; ctu=358c3bab65bdc03610c90ac12957311f187d89097d155d3ce9cfd474d0aea169; _dp.ac.v=cb00f964-5f8b-4fa7-b713-33a7e58986e7; dper=c7200e0e5cad71c4f5c501b88cfa988d1b199b603b8897af7eb1da91d82b41d51818df025a448bf422439ad3cfb50566dd89448385fa0c6f144028656f4410c000feef968d20be18114c56eb30957a0b6951d2d474490c12210b3626eaf7be18; uamo=15876505396; dplet=3fb92bd5642e22a7d48c68837a67c613; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604844574; _lxsdk_s=175a82ff0cd-82e-54d-024%7C%7C71',
}

hosts = {
    'zhihu': 'www.zhihu.com',
    'huashengju': 'www.huashengju.com',
    'dianping': 'www.dianping.com',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,sq;q=0.7,zh-TW;q=0.6',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    #'DNT':'1',
    'Upgrade-Insecure-Requests':'1',
    'Host':hosts['dianping'],
    'Referer':'https://www.huashengju.com/user-login.html',
    'User-Agent':'{0}'.format(random.sample(USER_AGENT_LIST, 1)[0]),
    'Cookie':cookies['dianping']
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
    session = requests.session()
    response = session.get('http://www.dianping.com/shop/HacjkwuG9NzO0WtL', headers=headers, verify=False)
    print(response)
    html_str = response.content.decode()
    print(html_str)

    selector = etree.HTML(html_str)
    content = selector.xpath('//div[@id="basic-info"]/h1/text()')
    for each in content:
        print(each)

    '''
    tel = selector.xpath('//div[@id="basic-info"]/p[@class="expand-info tel"]/text()')
    print(tel)
    for each in tel:
        print(each)
    '''


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
    session = requests.session()
    response = session.get('https://www.zhihu.com/people/zi-ruo-49-9/posts', headers=headers, verify=False)
    print(response)
    html_str = response.content.decode()
    print(html_str)

    selector = etree.HTML(html_str)
    #content = selector.xpath('//div[@class="List-item"]/div/h2/a/text()')
    content = selector.xpath('//h2[@class="ContentItem-title"]/a/text()')
    print(content)
    for each in content:
        print(each)

def test_cookie():
    session = requests.session()
    html_str = session.get('https://www.huashengju.com/designer-init.html', headers=headers, verify=False)
    print(html_str.content.decode())

if __name__ == '__main__':
    get_dianping()