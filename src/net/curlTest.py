#!/usr/bin/env python
#-*- coding:utf8 -*-
import sys
sys.path.append('../')
import pycurl
import io
import time
from util.TimeUtil import TimeUtil

def get_by_curl(url):
    print(pycurl.version_info())
    buffer = io.BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    # c.setopt(c.TIMEOUT, 1)
    c.setopt(c.TIMEOUT_MS, 200)
    c.setopt(c.WRITEDATA, buffer)
    try:
        c.perform()
    except pycurl.error as e:
        print("Curl error: ", e)
    c.close()

    # 打印响应内容
    print(buffer.getvalue().decode('utf-8'))

if __name__ == '__main__':
    start = time.perf_counter()
    get_by_curl('http://localhost:8085/blog/1')
    end = time.perf_counter()
    cost_time = TimeUtil.millisecond(start, end)
    print(f'send_req time: {cost_time}ms')

def get_qq():
    html = io.BytesIO()
    url = 'https://mail.qq.com/cgi-bin/loginpage'
    c = pycurl.Curl()
    c.setopt(pycurl.URL,url)
    c.setopt(pycurl.SSL_VERIFYHOST, False)
    c.setopt(pycurl.SSL_VERIFYPEER,False)
    c.setopt(pycurl.WRITEFUNCTION, html.write)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.perform()
    print(c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL))
    print(html.getvalue())

