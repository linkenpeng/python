# coding=utf-8
#/usr/bin/env python

"多线程下载文件"

from time import ctime
from myThread import MyThread
import urllib2
import urllib

def downFile(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html
	
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
        print(mThread[i].getResult())

fileUrls = ['http://img2.3lian.com/img2007/17/08/001.jpg','http://img2.3lian.com/img2007/17/08/002.jpg']
        
def main():
    mFunc(downFile, fileUrls)
     
if __name__ == '__main__':
    main()
    

