#/usr/bin/env python
#coding=gb2312

import sys
import os
import threading
import Queue
import csv

path = sys.path
o = sys.stdout
reload(sys)
sys.stdout = o
sys.path = path
sys.setdefaultencoding("gbk")

def allfiles():
    for root,dir,files in os.walk(r"f:\\"):
        for f in files:
            print(f)
    
def changeType():
    a=[1, 2, 3]
    return map(str, a)


def csvReader():
    os.chdir('C:\Users\Administrator\Desktop\python')
    reader=csv.reader(file('file.log'))
    queue=Queue.Queue()
    out_queue=Queue.Queue()   
    
    with open('file.log', 'rt') as f:
        reader = csv.reader(f)
        for i in reader:
            #print(i)
            queue.put(i)
        
    line=queue.get()
    for a in line:
        a,b,c=line[0],line[1],line[2]
        print(a,b,c)


if __name__ == '__main__' :
    allfiles()
    print(changeType())