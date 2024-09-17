#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# re.search 找到一个就返回
def search_test(html):
    groups = re.search('<li>(.*)</li>', html)
    print(groups)
    print(groups[0])
    print(groups[1])


def find_all_test(html):
    # compile效率高些
    partten = re.compile('<li>(.*?)</li>')
    groups2 = re.findall(partten, html)
    print(groups2)
    print(groups2[0])
    print(groups2[1])

def match_test():
    m = re.match('foo','foo')
    if m is not None:
        print(m.group())

    m = re.match('(\w\w\w)-(\d\d\d)','abc-123')
    print(m.group())

    partten = 'car'
    string_partten = 'a carefull car is coming'
    m = re.search(partten,string_partten)
    print(m.group())

    ps = 'Mon Jul  3 04:22:30 1972::vbyitfl@jpgxlpgpvdiy.net::78956550-7-12'
    pt1 = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
    m = re.match(pt1,ps)
    print(m.group())
    print(m.group(1))
    print(m.groups())


    li = re.split('@',ps)
    print(li)
    ps2 = re.sub('@','##', ps)
    print(ps2)

    pt2 = '\d+-\d+-\d+'
    m = re.search(pt2, ps)
    print(m.group())
    m = re.match('.+?('+pt2+')', ps)
    if m is not None:
        print(m.group(1))

def test2():
    s = '123abc4567xyzt'
    p = r'(\d*)([a-zA-Z]*)'
    m = re.match(p, s)
    print(m.group())
    m = re.findall(p, s)
    print(m)

def main():
    html = '''
        <div><ul><li>我是一个兵</li><ul></div>
        <div><ul><li>我是一个兵</li><ul></div>
    '''
    search_test(html)
    find_all_test(html)
    match_test()

if __name__ == '__main__':
    test2()





















