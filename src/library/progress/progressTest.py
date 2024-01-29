#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
pip install progress
'''
from progress.bar import Bar
n = 10000
with Bar('进度', max=n) as bar:
    for i in range(n):
        for j in range(n):
            k = i * j
        #print(f'{i + 1} / {n}', end='\r')
        bar.next()
print('Done')