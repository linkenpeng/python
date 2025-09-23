#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分桶测试
pip install pandas
"""
import pandas as pd
import sys
import os
sys.path.append(os.getcwd() + '/src')
from util.ConfigUtil import ConfigUtil
ConfigUtil = ConfigUtil()

def hashcode(s):
    h = 0
    for char in s:
        h = 31 * h + ord(char)
    return h

def bucketing():
    source_file = 'test_data/openid.csv'
    df = pd.read_csv(source_file)
    
    config = ConfigUtil.get_config('conf/prd.txt')
    scene_code = config['scene_code']

    INT_MAX = 2**31 - 1
    bucket = dict()
    list_ratio = [{"b":"A", "p":85}, {"b":"B", "p":5},{"b":"C", "p":5}, {"b":"D", "p":5}]
    result = dict()
    for open_id in sorted(df['open_id']):
        str = open_id + scene_code
        hash = hashcode(str) & INT_MAX
        ratio = hash % 100

        if ratio in bucket:
            bucket[ratio] += 1
        else:
            bucket[ratio] = 1
    
    current_range = 0
    current_loop = 1
    for l in list_ratio:
        current_range += l['p']
        b = l['b']
        # print(f"{b} = {current_range}")
        result[b] = 0
        for k, v in bucket.items():
            if current_loop == 1:
                if k < current_range:
                    result[b] += v
            else:
                if k < current_range and k >= current_range - l['p']:
                    result[b] += v

        current_loop += 1
    
    print(result)
    print(sum(result.values()))

if __name__ == '__main__': 
    bucketing()