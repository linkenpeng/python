#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
pip install fake_useragent
pip install requests beautifulsoup4 lxml

requests http请求库，可以替代 urllib2,3
Scrapy: 优秀的网络爬虫框架
pyspider: 强大的Web页面爬取系统

Beautiful Soup: HTML和XML的解析库
解析器：
- html.parser
- lxml
- lxml-xml
- html5lib

反爬与反反爬：
- Header限制
- 访问频率限制
- 模拟登录验证码
- IP限制
- Cookie要求与Cookie限制


Re:正则表达式解析和处理功能库
Python-Goose: 提取文章类型web页面的功能库
'''

import requests
import re
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
from random import randint

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
    data = {'username':'','passType':'code','passCode':'7964','action':'1'}
    html = requests.post('https://www.huashengju.com/?c=user&a=doLogin', data, headers=headers)
    print(html.content.decode())


def search_baidu(keyword):
    url = f'https://www.baidu.com/s?wd={keyword}'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'请求失败：{e}')
        return
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        results = soup.select('.result.c-container')
        for result in results:
            title = result.select_one('.t a')
            if title:
                print(title.text)
            else:
                print('无标题')
    else:
        print('请求失败')
    
    time.sleep(randint(1, 5))

def add_cookies():
    cookies="anonymid=j3jxk555-nrn0wh; _r01_=1; _ga=GA1.2.1274811859.1497951251; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; ln_uact=mr_mao_hacker@163.com; depovince=BJ; jebecookies=54f5d0fd-9299-4bb4-801c-eefa4fd3012b|||||; JSESSIONID=abcI6TfWH4N4t_aWJnvdw; ick_login=4be198ce-1f9c-4eab-971d-48abfda70a50; p=0cbee3304bce1ede82a56e901916d0949; first_login_flag=1; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20171230/1635/main_JQzq_ae7b0000a8791986.jpg; t=79bdd322e760beae79c0b511b8c92a6b9; societyguester=79bdd322e760beae79c0b511b8c92a6b9; id=327550029; xnsid=2ac9a5d8; loginfrom=syshome; ch_id=10016; wp_fold=0"
    cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}

if __name__ == '__main__':
    keyword = input('请输入搜索关键词：')
    search_baidu(keyword)