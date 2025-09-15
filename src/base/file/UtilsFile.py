# -*- coding: utf-8 -*-
#/usr/bin/env python

import os

class UtilsFile():
    def __init__(self, filename):
        self.filename = filename
    
    def getExt(self, filename):
		return filename[filename.rindex('.') + 1 : len(filename)]
	
    def makeDirs(self, filename):
		filename = filename.replace('\\', '/')
		if os.path.isdir(filename):
			dir = filename
		else:
			dir = filename[0 : filename.rindex('/')]
		if not os.path.exists(dir):
			os.makedirs(dir, 777)
    
    def writeFile(self, filename, content):
		self.makeDirs(filename)
		f = open(filename, 'wb')
		f.write(content)
		f.close()
    
if __name__ == '__main__': 
    file = UtilsFile('a.abc')
    print(file.getExt('a.abc'))
    pass