#!/usr/bin/env python
#-*- coding:utf8 -*-
import json
import sys
sys.path.append('../')
import pycurl
import io
import time
from util.TimeUtil import TimeUtil

def get_config():
    config = {}
    with open('../test_data/ra_config.txt') as file:
        for line in file:
            kv = line.split('=')
            config[kv[0]] = kv[1].strip('\n')
    return config

def get_test_data():
    with open('../test_data/ra_test_data.txt') as f:
        post_data = f.read()
    print(f'post_data: {post_data}')
    json_data = json.dumps(post_data)
    print(f'json_data: {json_data}')
    return json_data

def get_by_curl(post_json, url, config):
    # print(pycurl.version_info())
    buffer = io.BytesIO()
    c = pycurl.Curl()
    headers = [
        'Content-Type: application/json',
        'accessKey: ' + config['accessKey']
    ]
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
    config = get_config()
    url = config['url']
    post_data = get_test_data()
    get_by_curl(post_data, url, config)

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



