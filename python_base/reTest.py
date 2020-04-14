#!/usr/bin/env python

import re

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


