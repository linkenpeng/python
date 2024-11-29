#!/usr/bin/env python
#-*- coding:utf8 -*-
import sys
sys.path.append('../')
import time
import json
from util.TimeUtil import TimeUtil
from util.MockUtil import MockUtil
from util.SignUtil import SignUtil

import requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    "User-Agent": ua.random,
    "Content-Type": 'application/json'
}

def get_by_requests(url, data, headers):
    try:
        response = requests.post(url, data, headers=headers, timeout=(0.2, 0.2))
        print(response.content)
        if(response.content > 0):
            data = json.loads(response.content)
            return data
        else:
            return {}
    except Exception as ex:
        print(ex)
        return {}

if __name__ == '__main__':
    start = time.perf_counter()

    mock = MockUtil()
    config = mock.get_config('../test_data/ra_config.txt')
    url = config['url']
    current_time = time.time()
    milliseconds = str(int(round(current_time * 1000)))
    config['timestamp'] = milliseconds
    signUtil = SignUtil()
    authString = signUtil.get_auth_string(config)
    headers['timestamp'] = milliseconds
    headers['authString'] = authString
    headers['accessKey'] = config['accessKey']
    print(headers)
    post_data = mock.get_test_data('../test_data/ra_test_data.txt')

    get_by_requests(url, post_data, headers)

    end = time.perf_counter()
    cost_time = TimeUtil.millisecond(start, end)
    print(f'send_req time: {cost_time}ms')