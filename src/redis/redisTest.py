#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
redis 测试
'''

import redis

def test():
    client = redis.StrictRedis()
    client.lpush('chapter_6', 123)
    len = client.llen('chapter_6')
    print(len)

if __name__ == '__main__':
    test()