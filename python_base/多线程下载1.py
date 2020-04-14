#! /usr/bin/env python
#coding=utf-8

from __future__ import unicode_literals

import gevent
from gevent.threadpool import ThreadPool

# 注销后，感觉速度不变
#from gevent import monkey; monkey.patch_all()

import os
import sys
import cPickle
from collections import namedtuple
import urllib2
from urlparse import urlsplit

import time

# default parameters
defaults = dict(thread_count=50,
    buffer_size=10*1024,
    block_size=1000*1024)


def progress(percent, width=50):
    print "%s %d%%\r" % (('%%-%ds' % width) % (width * percent / 100 * '='), percent),
    if percent >= 100:
        print
        sys.stdout.flush()


def write_data(filepath, data):
    with open(filepath, 'wb') as output:
        cPickle.dump(data, output)


def read_data(filepath):
    with open(filepath, 'rb') as output:
        return cPickle.load(output)


FileInfo = namedtuple('FileInfo', 'url name size lastmodified')


def get_file_info(url):
    class HeadRequest(urllib2.Request):
        def get_method(self):
            return "HEAD"
    res = urllib2.urlopen(HeadRequest(url))
    res.read()
    headers = dict(res.headers)
    print headers
    size = int(headers.get('content-length', 0))
    lastmodified = headers.get('last-modified', '')
    name = None
    if headers.has_key('content-disposition'):
        name = headers['content-disposition'].split('filename=')[1]
        if name[0] == '"' or name[0] == "'":
            name = name[1:-1]
    else:
        name = os.path.basename(urlsplit(url)[2])

    return FileInfo(url, name, size, lastmodified)


def download(url, output, 
        thread_count = defaults['thread_count'], 
        buffer_size = defaults['buffer_size'], 
        block_size = defaults['block_size']):
    # get latest file info
    file_info = get_file_info(url)

    # init path
    if output is None:
        output = file_info.name
    workpath = '%s.ing' % output
    infopath = '%s.inf' % output

    # split file to blocks. every block is a array [start, offset, end],
    # then each greenlet download filepart according to a block, and 
    # update the block' offset.
    blocks = []

    if os.path.exists(infopath):
        # load blocks
        _x, blocks = read_data(infopath)        
        if (_x.url != url or 
                _x.name != file_info.name or 
                _x.lastmodified != file_info.lastmodified):
            blocks = []

    if len(blocks) == 0:
        # set blocks
        if block_size > file_info.size:
            blocks = [[0, 0, file_info.size]]
        else:
            block_count, remain = divmod(file_info.size, block_size)
            blocks = [[i*block_size, i*block_size, (i+1)*block_size-1] for i in range(block_count)]
            blocks[-1][-1] += remain
        # create new blank workpath
        with open(workpath, 'wb') as fobj:
            fobj.write('')

    # start monitor
    monitor = gevent.spawn(_monitor, infopath, file_info, blocks)
    
    # start downloading
    with open(workpath, 'rb+') as fobj:
        args = [(url, blocks[i], fobj, buffer_size) for i in range(len(blocks)) if blocks[i][1] < blocks[i][2]]

        if thread_count > len(args):
            thread_count = len(args)

        pool = ThreadPool(thread_count)
        pool.map(_worker, args)
        pool.join()

    monitor.join()

    # rename workpath to output
    if os.path.exists(output):
        os.remove(output)
    os.rename(workpath, output)

    # delete infopath
    if os.path.exists(infopath):
        os.remove(infopath)

    print 'thread_count ', thread_count


def _worker((url, block, fobj, buffer_size)):
    req = urllib2.Request(url)
    req.headers['Range'] = 'bytes=%s-%s' % (block[1], block[2])
    res = urllib2.urlopen(req)

    while 1:
        chunk = res.read(buffer_size)
        if not chunk:
            break
        fobj.seek(block[1])
        fobj.write(chunk)
        block[1] += len(chunk)  


def _monitor(infopath, file_info, blocks):
    while 1:
        percent = sum([block[1] - block[0] for block in blocks]) * 100 / file_info.size
        #print blocks[0:4]
        progress(percent)
        if percent >= 100:
            break            
        write_data(infopath, (file_info, blocks)) 
        gevent.sleep(2)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Download file by multi-threads.')
    parser.add_argument('url', type=str, help='url of the download file')
    parser.add_argument('-o', type=str, default=None, dest="output", help='output file')
    parser.add_argument('-t', type=int, default=defaults['thread_count'], dest="thread_count", help='thread counts to downloading')
    parser.add_argument('-b', type=int, default=defaults['buffer_size'], dest="buffer_size", help='buffer size')
    parser.add_argument('-s', type=int, default=defaults['block_size'], dest="block_size", help='block size')

    argv = sys.argv[1:]

    if len(argv) == 0:
        argv = ['https://eyes.nasa.gov/eyesproduct/EYES/os/win']

    args = parser.parse_args(argv)

    start_time = time.time()
    download(args.url, args.output, args.thread_count, args.buffer_size, args.block_size)
    print 'times:%r' % (time.time()-start_time)