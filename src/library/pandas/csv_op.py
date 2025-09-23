#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

def read():
    source_file = 'test_data/openid.csv'
    df = pd.read_csv(source_file)
    
    config = ConfigUtil.get_config('conf/prd.txt')
    scene_code = config['scene_code']

    INT_MAX = 2**31 - 1
    bucket = dict()
    list_ratio = [85, 5, 5, 5]
    result = dict()
    for open_id in df['open_id']:
        str = open_id + scene_code
        hash = hashcode(str) & INT_MAX
        ratio = hash % 100

        if ratio in bucket:
            bucket[ratio] += 1
        else:
            bucket[ratio] = 1
        
        """
        user_weight = 0
        for l in list_ratio:
            user_weight += l
            if l < user_weight:
                if l in result:
                    result[l] += 1
                else:
                    result[l] = 1
                break
        """


    #print(sum(bucket.values()))
    #print(sorted(bucket.keys()))
    #print(bucket)
    user_weight = 0
    for l in list_ratio:
        user_weight += l
        print(f"{l} = {user_weight}")
        result[l] = 0
        for k, v in bucket.items():
            if k < user_weight:
                result[l] += v
    
    print(result)
    
def write(data, output_file='output.csv'):
    """
    将数据写入 CSV 文件
    :param data: 要写入的数据（DataFrame 或字典）
    :param output_file: 输出文件路径，默认为 'output.csv'
    """
    if isinstance(data, pd.DataFrame):
        data.to_csv(output_file, index=False)
    elif isinstance(data, dict):
        pd.DataFrame(data).to_csv(output_file, index=False)
    else:
        raise ValueError("Unsupported data type. Expected DataFrame or dict.")

if __name__ == '__main__': 
    read()