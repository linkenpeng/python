#coding=gb2312
#/usr/bin/env python

'多线程下载'

import urllib2
import time
from myThread import MyThread

def downFile(url):
    response = urllib2.urlopen(url)
    content = response.read()
    return content
	
def mFunc(func, fileUrls):
    urlslen = range(len(fileUrls))
    mThread = []
    for i in urlslen:
        print('append: ', i)
        t = MyThread(func, (fileUrls[i],), func.__name__)
        mThread.append(t)
        
    for i in urlslen:
        print('start:' , i)
        mThread[i].start()
        
    for i in urlslen:
        print('join: ', i)
        mThread[i].join()
#        print(mThread[i].getResult())

fileUrls = ['http://img2.3lian.com/img2007/17/08/001.jpg',
            'http://img2.3lian.com/img2007/17/08/002.jpg',
            'http://img2.3lian.com/img2007/17/08/003.jpg',
            'http://img2.3lian.com/img2007/17/08/004.jpg',
            'http://img2.3lian.com/img2007/17/08/005.jpg',
            'http://img2.3lian.com/img2007/17/08/006.jpg',
            ]
        
def main():
    start = time.time()
    mFunc(downFile, fileUrls)
    end = time.time()
    print((end - start),'秒')
     
if __name__ == '__main__':
    main()
