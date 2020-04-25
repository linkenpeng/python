#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyquery import PyQuery as pq
from lxml import etree
import redis
import sys
import re
import urllib
import urllib2
import json
import hashlib
import random
import time
import os

hash_name = 'qiushibaike'
server_address = 'localhost'
img_base_path = '/data/img'

def getRandomFileName(ext):
    return chr(random.randint(97, 122)) + str(random.randint(10000,99999)) + str(time.time()).split('.')[0] + ext

def getHashPath():
    dirtotal = 99
    dirdepth = 3
    hashpath = ''
    for i in range(1, dirdepth):
        hashpath = hashpath + str(random.randint(1, dirtotal)) + '/'
    return hashpath
#发微博接口   
def sendData(args):
    url = 'http://a.b.c/weibo/send'
    args['account'] = 'qiushibaike@gmail.com'
    args['robot_type'] = 'gtalk'
    args['src'] = 20

    data = urllib.urlencode(args)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    r_data = response.read()
    json_data = json.loads(r_data)
    return json_data


ids = []
qb = pq('http://www.qiushibaike.com')
for i in qb('div[id^=qiushi_tag]'):
    m = re.match(r'[\w_]+?(\d+)$', qb(i).attr('id'))
    ids.append(m.group(1))
r_server = redis.Redis(server_address)
exists_list = r_server.hmget(hash_name, ids)
val_ids = {}
for i in range(len(ids)):
    if not exists_list[i]:
        val_ids[ids[i]] = 1

args = {}
url = ''
ext = ''
count = 1
for i in val_ids.keys():
    a = 'qiushi_tag_' + i
    args['act'] = 'addWeibo'
    args['content'] = qb('#' + a).find('div.content').text()
    args['pic'] = ''
    args['qid'] = '102251'
    if count == 1:
        args['extra_weibo'] = '1'
    else:
        args['extra_weibo'] = ''

    if qb('#' + a).find('div.thumb'):
        url = qb('#' + a).find('div.thumb img').attr('src')
        print 'download img from:' + url
        ext = os.path.splitext(url)[1]
        print 'img ext: ' + ext
        path = getHashPath()
        full_path = img_base_path + path
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        filename = getRandomFileName(ext)
        ab_path = full_path + filename
        urllib.urlretrieve(url, ab_path)
        args['pic'] = '/weibo/' + path + filename
        print 'img:' + url + ' save file:' + ab_path
    print args
    ret = sendData(args)
    if not int(ret['errcode']):
        del val_ids[i]    
    print args['content']
    count += 1
    if count > 5:
        time.sleep(61)
        count = count % 5
    else:
        time.sleep(2)
    
        
if len(val_ids):
    r_server.hmset(hash_name, val_ids)