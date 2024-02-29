
#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
pip install qianfan
'''
import os
import requests
import re
from fake_useragent import UserAgent
import redis
import json

os.environ["QIANFAN_ACCESS_KEY"] = ""
os.environ["QIANFAN_SECRET_KEY"] = ""

ua = UserAgent()
headers = {
 "User-Agent": ua.random
}

def get_redis_client():
    client = redis.StrictRedis(host='', port='6379')
    return client

def get_access_token():
    redis = get_redis_client()
    cache_key = 'test:qianfan:access_token'
    cache_value = redis.get(cache_key)
    # print(f"get from cache: {cache_value}")
    if(len(cache_value) > 0):
        print(cache_value.access_token)
        return cache_value

    access_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'
    ACCESS_KEY = os.environ["QIANFAN_ACCESS_KEY"]
    SECRET_KEY = os.environ["QIANFAN_SECRET_KEY"]
    token_url = access_token_url % (ACCESS_KEY, SECRET_KEY)

    data = {}
    response = requests.post(token_url, data, headers=headers)
    if(response.content > 0):
        redis.set(cache_key, response.content, ex=response.content['expires_in'])
        return response.content
    else:
        return {}

if __name__ == '__main__':
    token_info = get_access_token()