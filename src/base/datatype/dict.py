#!/usr/bin/env python
#-*- coding:utf8 -*-

def init():
    d = {} # 定义空字典
    d = dict() # 定义空字典
    d = {'a': 1, 'b': 2, 'c': 3}
    d = {'a': 1, 'a': 1, 'a': 1} # {'a': 1} key不能重复，重复时取最后一个
    d = {'a': 1, 'b': {'x': 3}} # 嵌套字典
    d = {'a': [1,2,3], 'b': [4,5,6]} # 嵌套列表

    # 以下均可定义如下结果
    # {'name': 'Tom', 'age': 18, 'height': 180}
    d = dict(name='Tom', age=18, height=180)
    d1 = dict([('name', 'Tom'), ('age', 18), ('height', 180)])
    dict2 = dict(zip(['name', 'age', 'height'], ['Tom', 18, 180]))

    d['name']  # 'Tom'（获取键的值）
    d['age'] = 20  # 将age的值更新为20
    d['Female'] = 'man'  # 增加属性
    d.get('height', 180)  # 180

    # 嵌套取值
    d = {'a': {'name': 'Tom', 'age':18}, 'b': [4,5,6]}
    d['b'][1] # 5
    d['a']['age'] # 18

    d.pop('name') # 'Tom'（删除指定key）
    d.popitem() # 随机删除某一项
    del d['name']  # 删除键值对
    d.clear()  # 清空字典

    # 按类型访问，可迭代
    d.keys() # 列出所有键
    d.values() # 列出所有值
    d.items() # 列出所有键值对元组（k, v）

    # 操作
    d.setdefault('a', 3) # 插入一个键并给定默认值3，如不指定，则为None
    d1.update(dict2) # 将字典dict2的键值对添加到字典dict
    # 如果键存在，则返回其对应值；如果键不在字典中，则返回默认值
    d.get('math', 100) # 100
    d2 = d.copy() # 深拷贝，d变化不影响d2

    d = {'a': 1, 'b': 2, 'c': 3}
    max(d) # 'c'（最大的键）
    min(d) # 'a'（最小的键）
    len(d) # 3（字典的长度）
    str(d) # "{'a': 1, 'b': 2, 'c': 3}"（字符串形式）
    any(d) # True（只要一个键为True）
    all(d) # True（所有键都为True）
    sorted(d) # ['a', 'b', 'c']（所有键的列表排序）

def test():
    fdict = dict((['x',1],['y',2]))
    print(fdict)

    ddict = {}.fromkeys(('x','y'), -1)
    print(ddict)

    edict = {}.fromkeys(('foo','bar'))
    print(edict)

    dict2 = {'name': 'earch', 'port':80}
    for key in dict2.keys():
        print('key=%s, value=%s' % (key, dict2[key]))

    for key in dict2:
        print('key=%s, value=%s' % (key, dict2[key]))

    print(dict2['name'])

    print('host %s is running on port %d' % (dict2['name'], dict2['port']))

    #print(dict2['server'])
    print('server' in dict2)
    print('x' in fdict)

    dict3 = {}
    dict3[1] = 'abc'
    dict3['1'] = 3.1415926
    dict3[3.2] = 'xyz'
    print(dict3)

    dict2['name'] = 'venus'
    dict2['port'] = 6069
    dict2['arch'] = 'sunos5'
    print('host %(name)s is running on port %(port)d' % dict2)

    del dict2['name']
    print(dict2)
    #dict2.clear()
    print(dict2)
    print(dict2.pop('arch'))
    print(dict2)
    del dict2
    #print(dict2) error

    print(type(dict3))

    dict1 = {}
    dict2 = {'host':'earch','port':80}
    print(dict2.keys())
    print(dict2.values())
    print(dict2.items())
    print(dict1)
    dict1.update(dict2)
    print(dict1)
    dict4 = dict2.copy()
    print(dict4)

def test2():
    dc = {"a":1, "b":2, "c": 3, "d":4}

    print(dc)
    print(dc["a"])
    print(type(dc))

    del dc['a'];

    print(dc)

    print("b" in dc)

    print(dc.keys())

    print(dc.values())

    print(dc.items())

    print(dc.get("a", 11))

    print(dc.pop("b", 22))

    print(dc.popitem())

    print(len(dc))

    dc.clear()

    print(dc)
    
if __name__ == '__main__':
    init()







