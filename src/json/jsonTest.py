#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
json 测试
'''
import os
import json

def test_json():
    person = {'basic_info': {'name': 'kingname','age': 24,'sex': 'male','merry': False},'work_info': {'salary': 99999,'position': 'engineer','department': None}}
    print(person['basic_info']['name'])

    person_json = json.dumps(person)
    print(person_json)

    person_json_indent = json.dumps(person, indent=4)
    print(person_json_indent)

def walk(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            walk(v, f"{path}/{k}")
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            walk(item, f"{path}[{idx}]")
    else:
        print(path, "=>", obj)

def convertData():
    print(os.getcwd())
    with open('src/test_data/cityData.json', 'r') as f:
        data = f.read()
    jsonData = json.loads(data)
    walk(jsonData)

if __name__ == '__main__':
    convertData()