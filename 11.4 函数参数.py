#!/usr/bin/env python

#from urllib import urlretrieve
import urllib.request

def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
    else:
        return eachLine
    
def firstLast(webpage):
    pass
#    f = open(webpage)
#    lines = f.readlines()
#    f.close()
#    print(firstNonBlank(lines))
#    lines.reverse()
#    print(firstNonBlank(lines))

def download(url='http://www.baidu.com', process=firstLast):
    try:
        f = urllib.request.urlopen(url)[0]
        print(f.read(100).decode('utf-8'))
    except IOError:
        retval = None
    if retval:
        process(retval)
        
if __name__ == '__main__':
    download()

            
            
            
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    



