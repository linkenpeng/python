#coding=gb2312
#/usr/bin/env python

'多线程下载'

import urllib2
import time
import os 
from myThread import MyThread

def downFile(url):
    response = urllib2.urlopen(url)
    content = response.read()
    return content
	
def writeFile(filename, content):
    makeDirs(filename)
    f = open(filename, 'wb')
    f.write(content)
    f.close()
    
def makeDirs(filename):
    filename = filename.replace('\\','/')
    if os.path.isdir(filename):
         dir = filename
    else:
        dir = filename[0 : filename.rindex('/')]        
    if not os.path.exists(dir):
        os.makedirs(dir, 0777)
    
def mFunc(func, fileUrls):
    urlslen = range(len(fileUrls))
    mThread = []
    for i in urlslen:
        t = MyThread(func, (fileUrls[i],), func.__name__)
        mThread.append(t)
        
    for i in urlslen:
        mThread[i].start()
        
    for i in urlslen:
        mThread[i].join()
        writeFile(fileUrls[i].replace('http://',os.getcwd()), mThread[i].getResult())

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
    print((end - start),'S')
     
if __name__ == '__main__':
    main()
