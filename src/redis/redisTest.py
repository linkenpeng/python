#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
redis 测试
'''

import redis
import json

def get_client():
    client = redis.StrictRedis(host='localhost', port='6379')
    return client

def list_op():
    ids = list()
    with open('../test_data/test.txt') as f:
        for line in f:
            ids.append(line.replace('\n', ''))
    json_data = json.dumps(ids)
    print(json_data)
    
    redis = get_client()
    redis.set('ids', json_data)
    

def string():
    client = get_client()

    client.set('k1', 'v1')
    print(client.get('k1'))
    #client.delete('k1')
    print(client.setnx('k1', 'v1'))

    client.mset({'k2':'v2','k3':'v3'})
    print(client.mget('k1','k2'))

    client.set('k4', 1)
    print(client.get('k4'))
    for i in range(5):
        client.incr('k4', 1)
    print(client.get('k4'))

    for i in range(3):
        client.decr('k4', 1)
    print(client.get('k4'))

def collection():
    client = get_client()
    client.lpush('chapter_6', 123)
    value = client.lpop('chapter_6')
    print(value)

    client.sadd('url', 'www.baidu.com')
    client.sadd('url', 'www.qq.com')
    client.sadd('url', 'www.163.com')

    url = client.spop('url')
    print(url)

    length = client.scard('url')
    print(length)

    urls = client.smembers('url')
    for i in urls:
        print(i)

if __name__ == '__main__':
    list_op()