#!/usr/bin/env python

'readTextFile.py -- read and display text file'

# get filename
fname = input('Enter filename: ')
print()

# attempt to open file for reading
try:
    fobj = open(fname,'r')
except IOError as e:
    print("*** file openerror:", e)
else:
    # display contents to the screeen
    for eachLine in fobj:
        print(eachLine,end=' ')
    fobj.close()