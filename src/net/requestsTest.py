#!/usr/bin/env python
#-*- coding:utf8 -*-
import sys
sys.path.append('../')
import time
import json
from util.TimeUtil import TimeUtil

import requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    "User-Agent": ua.random
}

def get_by_requests(url):
    data = {}
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
    get_by_requests('http://localhost:8085/blog/1')
    end = time.perf_counter()
    cost_time = TimeUtil.millisecond(start, end)
    print(f'send_req time: {cost_time}ms')