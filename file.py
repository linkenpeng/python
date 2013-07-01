#! /usr/bin/env python
#coding=utf-8

import urllib2
import os 
print os.getcwd()
response = urllib2.Request('http://picm.photophoto.cn/015/037/003/0370030333.jpg');
rs = urllib2.urlopen(response)
f = open("pic.jpg",'wb')
f.write(rs.read());
f.close();

