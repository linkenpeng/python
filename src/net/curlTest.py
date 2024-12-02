#!/usr/bin/env python
#-*- coding:utf8 -*-
import sys
sys.path.append('../')
import pycurl
import io
import time
from util.TimeUtil import TimeUtil
from util.MockUtil import MockUtil
from util.SignUtil import SignUtil

def get_by_curl(post_json, url, headers):
    # print(pycurl.version_info())
    buffer = io.BytesIO()
    c = pycurl.Curl()
    # 设置HTTP头部
    # c.setopt(c.HTTPHEADER, headers)
    c.setopt(c.HTTPHEADER, headers)
    c.setopt(c.URL, url)
    c.setopt(c.TIMEOUT, 1)
    # c.setopt(c.TIMEOUT_MS, 200)
    c.setopt(c.POSTFIELDS, post_json)
    c.setopt(c.WRITEDATA, buffer)
    try:
        c.perform()
    except pycurl.error as e:
        print("Curl error: ", e)
    c.close()

    # 打印响应内容
    print(buffer.getvalue().decode('utf-8'))

def request():
    mock = MockUtil()
    config = mock.get_config('../test_data/ra_config.txt')
    url = config['url']
    current_time = time.time()
    milliseconds = str(int(round(current_time * 1000)))
    config['timestamp'] = milliseconds
    signUtil = SignUtil()
    authString = signUtil.get_auth_string(config)
    headers = [
        'Content-Type:application/json',
        #'timestamp: ' + milliseconds,
        #'authString: ' + authString,
        #'accessKey: ' + config['accessKey']
    ]
    print(headers)
    post_data = mock.get_test_data('../test_data/ra_test_data.txt')
    get_by_curl(post_data, url, headers)

def get_ssl_data(url = 'https://mail.qq.com/cgi-bin/loginpage'):
    html = io.BytesIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL,url)
    c.setopt(pycurl.SSL_VERIFYHOST, False)
    c.setopt(pycurl.SSL_VERIFYPEER,False)
    c.setopt(pycurl.WRITEFUNCTION, html.write)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.perform()
    print(c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL))
    print(html.getvalue())

if __name__ == '__main__':
    start = time.perf_counter()
    request()
    end = time.perf_counter()
    cost_time = TimeUtil.millisecond(start, end)
    print(f'send_req time: {cost_time}ms')



