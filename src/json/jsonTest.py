#!/usr/bin/env/ python
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

     # 读取原始JSON文件
    try:
        with open('src/test_data/cityData.json', 'r', encoding='utf-8') as f:
            jsonData = json.load(f)
    except FileNotFoundError:
        print("cityData.json 文件不存在")
        return
    except json.JSONDecodeError:
        print("JSON格式错误")
        return

    # 将原始数据转换为Python对象
    for province in jsonData:
        cities = province.get('cities', [])
        if cities:  # 确保城市列表不为空
            first_city_salary = cities[0].get('avgSalary')
            # 将该省份所有城市的avgSalary设置为第一个城市的avgSalary
            for city in cities:
                city['avgSalary'] = first_city_salary
    
    # 将修改后的数据保存到新的JSON文件
    try:
        with open('src/test_data/modifiedCityData.json', 'w', encoding='utf-8') as f:
            json.dump(jsonData, f, ensure_ascii=False, indent=2)
        print("修改后的数据已保存到 modifiedCityData.json")
    except Exception as e:
        print(f"保存文件时出错: {e}")

if __name__ == '__main__':
    convertData()
    #modify_city_salaries()