#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
mongodb 测试
'''


from pymongo import MongoClient

def get_collection(db_name, col_name):
    client = MongoClient()
    database = client[db_name]
    collection = database[col_name]
    return collection

def insert():
    collection = get_collection('smile', 'log')

    data = {'id': 1, 'name': 'kingname', 'age': 28, 'salary': 30000}
    collection.insert_one(data)

    more_data = [
                 {'id': 2,'name': '张三','age': 22,'salary': 5000},
                 {'id': 3, 'name': '李四', 'age': 30, 'salary': 9000},
                 {'id': 4, 'name': '李四', 'age': 25, 'salary': 15000},
                 {'id': 5, 'name': '李四', 'age': 33, 'salary': 35000},
                 ]
    collection.insert_many(more_data)

def find():
    collection = get_collection('smile', 'log')
    content = collection.find()
    for i in content:
        print(i)

    print('--' * 60)
    content = collection.distinct('name')
    for i in content:
        print(i)

    print('--' * 60)
    content = collection.find({'age': 22})
    for i in content:
        print(i)

    print('--' * 60)
    content = collection.find({'age': {'$gt': 20}}) # > 20
    for i in content:
        print(i)

    print('--' * 60)
    content = collection.find({'age': {'$gte': 28, '$lte': 30}}) #>=28 && <=30
    for i in content:
        print(i)

def delete():
    collection = get_collection('smile', 'log')
    collection.delete_one({'name': 'kingname'})
    collection.delete_many({'name': '李四'})

def update():
    collection = get_collection('smile', 'log')
    collection.update_one({'age': 10}, {'$set': {'salary': 1000}})
    collection.update_many({'name': '张三'}, {'$set': {'age': 20}})

if __name__ == '__main__':
    # insert()
    # delete()
    # update()
    find()