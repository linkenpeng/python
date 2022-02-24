# coding=gb2312
#!/usr/bin/env python

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

if __name__ == '__main__':
    test()







