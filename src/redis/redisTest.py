#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
redis 测试
'''

import redis
import json
import gzip
import io
import time

def get_client():
    client = redis.StrictRedis(host='localhost', port='6379', password='')
    return client

# 压缩数据
def compress_data(data):
    buffer = io.BytesIO()
    bytes_data = data.encode('utf-8')
    with gzip.GzipFile(fileobj=buffer, mode='wb') as gz_file:
        gz_file.write(bytes_data)
    return buffer.getvalue()

# 解压数据
def decompress_data(compressed_data):
    buffer = io.BytesIO(compressed_data)
    with gzip.GzipFile(fileobj=buffer) as gz_file:
        hex_str = gz_file.read()
        return hex_str
    
def write_list():
    ids_500 = list()
    ids_20 = list()
    with open('../test_data/test.txt') as f:
        c = 0
        for line in f:
            ids_500.append(line.replace('\n', ''))
            if (c < 20):
                ids_20.append(line.replace('\n', ''))
            c+=1
    json_data_500 = '2_101058726,'.join(ids_500)
    json_data_20 = '2_101058726,'.join(ids_20)
    print(json_data_500)
    print(json_data_20)

    redis = get_client()
    redis.set('spus_500', json_data_500)
    redis.set('spus_20', json_data_20)

    start = time.perf_counter()
    gz_json_data_500 = compress_data(json_data_500)
    gz_json_data_20 = compress_data(json_data_20)
    end = time.perf_counter()
    print('gzip time:{}ms'.format((end - start)*1000))

    redis.set('spus_gz_500', gz_json_data_500)
    redis.set('spus_gz_20', gz_json_data_20)

def read_one(key):
    redis = get_client()
    compress_data = redis.get(key)
    print(compress_data)

    start = time.perf_counter()
    unzip_data = decompress_data(compress_data)
    end = time.perf_counter()
    print('un_gzip time:{}ms'.format((end - start)*1000))
    print(unzip_data)

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
    #write_list()
    read_one('spus_gz_500')
