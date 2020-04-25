#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
json 测试
'''

import json

def test_json():
    person = {'basic_info': {'name': 'kingname','age': 24,'sex': 'male','merry': False},'work_info': {'salary': 99999,'position': 'engineer','department': None}}
    print(person['basic_info']['name'])

    person_json = json.dumps(person)
    print(person_json)

    person_json_indent = json.dumps(person, indent=4)
    print(person_json_indent)

if __name__ == '__main__':
    test_json()