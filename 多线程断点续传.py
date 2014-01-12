#! /usr/bin/env python
#coding=utf-8

from __future__ import unicode_literals

from multiprocessing.dummy import Pool as ThreadPool
import threading
import time
import os
import sys
from collections import namedtuple
import cPickle

import urllib2

# 下载信息 tuple 类型
DownloadInf = namedtuple('DownloadInf', 'url filepath total blocks')

# 下载信息
download_inf = None

# 默认参数
defaults = dict(thread_count=10,
    buffer_size=500*1024,
    block_size=2000*1024)

# 全局锁
lock = threading.Lock()


def progress(percent, width=50):
    '''打印进度'''
    print "%s %d%%\r" % (('%%-%ds' % width) % (width * percent / 100 * '='), percent),
    if percent >= 100:
        print
        sys.stdout.flush()


def write_data(filepath, data):
    '''保存数据'''
    with open(filepath, 'wb') as output:
        cPickle.dump(data, output)


def read_data(filepath):
    '''读取数据'''
    with open(filepath, 'rb') as output:
        return cPickle.load(output)


def get_file_name(url):
    '''网络文件名称'''
    filename = os.path.basename(url)
    x = filename.find('?')
    if x > 0:
        filename = filename[:x]
    return filename

                
def get_file_size(url):
    '''网络文件大小'''
    class HeadRequest(urllib2.Request):
        def get_method(self):
            return "HEAD"

    res = urllib2.urlopen(HeadRequest(url))
    res.read()
    return int(dict(res.headers).get('content-length', 0))


def _downloading((i, fobj, buffer_size)):
    '''下载线程'''
    global download_inf

    url = download_inf.url
    block = download_inf.blocks[i]

    if block[1] >= block[2]:
        return

    req = urllib2.Request(url)
    # bytes=offset-end
    req.headers['Range'] = 'bytes=%s-%s' % (block[1], block[2])
    res = urllib2.urlopen(req)

    while 1:
        chunk = res.read(buffer_size)
        if not chunk:
            break
        with lock:
            fobj.seek(block[1])
            fobj.write(chunk)

            # update offset
            block[1] += len(chunk)     


def _monitor():
    '''监视下载进度'''
    global download_inf
    while 1:
        with lock:
            percent = sum([block[1] - block[0] for block in download_inf.blocks]) * 100 / download_inf.total
            progress(percent)
            if percent >= 100:
                break            
            write_data('%s.inf' % download_inf.filepath, download_inf) 
        time.sleep(1)


def download(url, filepath = None, 
        thread_count = defaults['thread_count'], 
        buffer_size = defaults['buffer_size'], 
        block_size = defaults['block_size'], ext='.ing'):

    global download_inf 

    if filepath is None:
        filepath = os.path.join('.', get_file_name(url))

    # 下载时，保存的文件路径
    workpath = '%s%s' % (filepath, ext)

    # 下载信息文件路径
    infpath = '%s.inf' % filepath
   
    if os.path.exists(infpath):
        # 存在下载信息文件，则读取
        download_inf = read_data(infpath)
    else:
        # 远端文件大小
        total = get_file_size(url)

        # 每个block大小，余量
        block_count, remain = divmod(total, block_size)

        #分块信息
        blocks = []
        for i in range(block_count):
            # 分块名称
            name = 'block_%d' % (i+1)
            # 开始位置
            start = i * block_size
            # 偏移位置，（下载开始时等于start, 随着下载, 不断增加）
            offset = start
            # 结束位置
            end = (i + 1) * block_size - 1
            if i == block_count - 1:
                # 最后一个加上余量
                end = (i + 1) * block_size + remain
            #线程信息需要下载时更新，用数组表示
            blocks.append([start, offset, end]) 
 
        download_inf = DownloadInf(url=url, filepath=filepath, total=total, blocks=blocks)

        # 建立空文件
        with open(workpath, 'wb') as fobj:
            fobj.write('')
    
    print 'downloading %s' % os.path.basename(filepath) 

    # 开始监视下载
    threading.Thread(target=_monitor).start() 

    # 断点续传，只能以"rb+" 形式打开文件
    with open(workpath, 'rb+') as fobj:
        blocks = download_inf.blocks
        args = [(i, fobj, buffer_size) for i in range(len(blocks)) if blocks[i][1] != blocks[i][2]]

        if thread_count > len(args):
            thread_count = len(args)

        pool = ThreadPool(thread_count)
        pool.map(_downloading, args)
        pool.close()
        pool.join()

    # 更名
    if os.path.exists(filepath):
        os.remove(filepath)
    os.rename(workpath, filepath)

    # 删除信息文件
    if os.path.exists(infpath):
        os.remove(infpath)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Download file by multi-threads.')
    parser.add_argument('url', type=str, help='url of the download file')
    parser.add_argument('-o', type=str, default=None, dest="filepath", help='output file')
    parser.add_argument('-t', type=int, default=defaults['thread_count'], dest="thread_count", help='thread counts to downloading')
    parser.add_argument('-b', type=int, default=defaults['buffer_size'], dest="buffer_size", help='buffer size')
    parser.add_argument('-s', type=int, default=defaults['block_size'], dest="block_size", help='block size')

    argv = sys.argv[1:]

    args = parser.parse_args(argv)

    download(args.url, args.filepath, args.thread_count, args.buffer_size, args.block_size)
