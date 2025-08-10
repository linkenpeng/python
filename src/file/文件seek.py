# -*- coding: utf-8 -*-
#/usr/bin/env python (1)起始行

f = open("test.txt","w+")
print(f.tell())
f.write('test line 1\n\r')
print(f.tell())
f.write('test line 2\n\r')
print(f.tell())

#f.seek(-14,1)
print(f.tell())

data = [line.strip() for line in f]

f.close()
