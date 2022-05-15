# coding=gb2312
#/usr/bin/env python (1)起始行

import sys

print('you entered',len(sys.argv),'armuments')
print('they were: ',str(sys.argv))

sys.stdout.write('Hello World!\n')
print(sys.platform)
print(sys.version)

print(dir(sys))
print(help(sys))
print(str(sys))
print(type(sys))
