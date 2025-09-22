#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import ssl
import hashlib
ssl._create_default_https_context = ssl._create_unverified_context

def hashcode(s):
    h = 0
    for char in s:
        h = 31 * h + ord(char)
    return h

def read():
    source_file = 'src/test_data/openid.csv'
    df = pd.read_csv(source_file)
    #print(df['open_id'])
    scene_code = "Pk7jNNS5HDMRtK1L4laj"
    JAVA_STYLE_MAX = 2**31 - 1
    bucket = dict()
    list_ration = [85, 5, 5, 5]
    for open_id in df['open_id']:
        str = open_id + scene_code
        hash_range = hashcode(str)
        hash = hash_range & JAVA_STYLE_MAX
        ration = hash % 100
        if ration in bucket:
            bucket[ration] += 1
        else:
            bucket[ration] = 1

    user_weight = 0
    result = dict()
    for l in list_ration:
        user_weight += l
        print(user_weight)
        result[l] = 0
        for k, v in bucket.items():
            if k <= user_weight:
                result[l] += v
        
    print(result)
    
def write():
    pass

if __name__ == '__main__': 
    read()