#!/usr/bin/env python
#-*- coding:utf8 -*-

import pycurl
import StringIO

print(pycurl.version_info())

html = StringIO.StringIO()
url = 'https://mail.qq.com/cgi-bin/loginpage'
c = pycurl.Curl()
c.setopt(pycurl.URL,url)
c.setopt(pycurl.SSL_VERIFYHOST, False)
c.setopt(pycurl.SSL_VERIFYPEER,False)
c.setopt(pycurl.WRITEFUNCTION, html.write)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.perform()
print(c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL))
print(html.getvalue())

