#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename: paxel.py
 
'''It is a multi-thread downloading tool
 
    It was developed follow axel.
        Author: volans
        E-mail: volansw [at] gmail.com
'''
 
import sys
import os
import time
import urllib
from threading import Thread
 
local_proxies = {'http': 'http://10.10.121.83:1918'}
 
class AxelPython(Thread, urllib.request.FancyURLopener):
    '''Multi-thread downloading class.
 
        run() is a vitural method of Thread.
    '''
    def __init__(self, threadname, url, filename, ranges=0, proxies={}):
        Thread.__init__(self, name=threadname)
        urllib.request.FancyURLopener.__init__(self, proxies)
        self.name = threadname
        self.url = url
        self.filename = filename
        self.ranges = ranges
        self.downloaded = 0
 
    def run(self):
        '''vertual function in Thread'''
        try:
            self.downloaded = os.path.getsize( self.filename )
        except OSError:
            #print 'never downloaded'
            self.downloaded = 0
 
        # rebuild start poind
        self.startpoint = self.ranges[0] + self.downloaded
 
        # This part is completed
        if self.startpoint >= self.ranges[1]:
            print ('Part %s has been downloaded over.') % self.filename
            return
 
        self.oneTimeSize = 16384 #16kByte/time
        print ('task %s will download from %d to %d') % (self.name, self.startpoint, self.ranges[1])
 
        self.addheader("Range", "bytes=%d-%d" % (self.startpoint, self.ranges[1]))
 
        self.urlhandle = self.open( self.url )
 
        data = self.urlhandle.read( self.oneTimeSize )
        while data:
            filehandle = open( self.filename, 'ab+' )
            filehandle.write( data )
            filehandle.close()
 
            self.downloaded += len( data )
            #print "%s" % (self.name)
            #progress = u'\r...'
 
            data = self.urlhandle.read( self.oneTimeSize )
 
def GetUrlFileSize(url, proxies={}):
    urlHandler = urllib.request.urlopen( url, proxies=proxies )
    headers = urlHandler.info().headers
    length = 0
    for header in headers:
        if header.find('Length') != -1:
            length = header.split(':')[-1].strip()
            length = int(length)
    return length
 
def SpliteBlocks(totalsize, blocknumber):
    blocksize = totalsize/blocknumber
    ranges = []
    for i in range(0, blocknumber-1):
        ranges.append((i*blocksize, i*blocksize +blocksize - 1))
    ranges.append(( blocksize*(blocknumber-1), totalsize -1 ))
 
    return ranges
def islive(tasks):
    for task in tasks:
        if task.isAlive():
            return True
    return False
 
def paxel(url, output, blocks=6, proxies=local_proxies):
    ''' paxel
    '''
    size = GetUrlFileSize( url, proxies )
    ranges = SpliteBlocks( size, blocks )
 
    threadname = [ "thread_%d" % i for i in range(0, blocks) ]
    filename = [ "tmpfile_%d" % i for i in range(0, blocks) ]
 
    tasks = []
    for i in range(0,blocks):
        task = AxelPython( threadname[i], url, filename[i], ranges[i] )
        task.setDaemon( True )
        task.start()
        tasks.append( task )
 
    time.sleep( 2 )
    while islive(tasks):
        downloaded = sum( [task.downloaded for task in tasks] )
        process = downloaded/float(size)*100
        show = '\rFilesize:%d Downloaded:%d Completed:%.2f%%' % (size, downloaded, process)
        sys.stdout.write(show)
        sys.stdout.flush()
        time.sleep( 0.5 )
 
    filehandle = open( output, 'wb+' )
    for i in filename:
        f = open( i, 'rb' )
        filehandle.write( f.read() )
        f.close()
        try:
            os.remove(i)
            pass
        except:
            pass
 
    filehandle.close()
 
if __name__ == '__main__':
    url = "http://10.10.121.83:1918/webservice/public/home/DM4940_KSD_11100614160x0000.bin"
    output = 'DM4940_KSD_11100614160x0000.bin'
    paxel( url, output, blocks=4, proxies={} )