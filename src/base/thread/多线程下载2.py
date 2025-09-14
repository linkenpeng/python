# -*- coding: utf-8 -*-
# Author: ToughGuy
# Email: wj0630@gmail.com
# 写这玩意儿是为了初步了解下python的多线程机制
# 平时没写注释的习惯, 这次花时间在代码里面写上注释也是希望有问题的地方请各位指正, 因为可能我自己也没弄明白.
# 测试平台 Ubuntu 13.04 X86_64 Python 2.7.4

import threading
import urllib2
import sys

max_thread = 10
# 初始化锁
lock = threading.RLock()

class Downloader(threading.Thread):
    def __init__(self, url, start_size, end_size, fobj, buffer):
        self.url = url
        self.buffer = buffer
        self.start_size = start_size
        self.end_size = end_size
        self.fobj = fobj
        threading.Thread.__init__(self)

    def run(self):
        """
            马甲而已
        """
        with lock:
            print 'starting: %s' % self.getName()
        self._download()

    def _download(self):
        """
            我才是搬砖的
        """
        req = urllib2.Request(self.url)
        # 添加HTTP Header(RANGE)设置下载数据的范围
        req.headers['Range'] = 'bytes=%s-%s' % (self.start_size, self.end_size)
        f = urllib2.urlopen(req)
        # 初始化当前线程文件对象偏移量
        offset = self.start_size
        while 1:
            block = f.read(self.buffer)
            # 当前线程数据获取完毕后则退出
            if not block:
                with lock:
                    print '%s done.' % self.getName()
                break
            # 写如数据的时候当然要锁住线程
            # 使用 with lock 替代传统的 lock.acquire().....lock.release()
            # 需要python >= 2.5
            with lock:
                sys.stdout.write('%s saveing block...' % self.getName())
                # 设置文件对象偏移地址
                self.fobj.seek(offset)
                # 写入获取到的数据
                self.fobj.write(block)
                offset = offset + len(block)
                sys.stdout.write('done.\n')


def main(url, thread=3, save_file='', buffer=1024):
    # 最大线程数量不能超过max_thread
    thread = thread if thread <= max_thread else max_thread
    # 获取文件的大小
    req = urllib2.urlopen(url)
    size = int(req.info().getheaders('Content-Length')[0])
    # 初始化文件对象
    fobj = open(save_file, 'wb')
    # 根据线程数量计算 每个线程负责的http Range 大小
    avg_size, pad_size = divmod(size, thread)
    plist = []
    for i in xrange(thread):
        start_size = i*avg_size
        end_size = start_size + avg_size - 1
        if i == thread - 1:
            # 最后一个线程加上pad_size
            end_size = end_size + pad_size + 1
        t = Downloader(url, start_size, end_size, fobj, buffer)
        plist.append(t)

    #  开始搬砖
    for t in plist:
        t.start()

    # 等待所有线程结束
    for t in plist:
        t.join()

    # 结束当然记得关闭文件对象
    fobj.close()
    print 'Download completed!'

if __name__ == '__main__':
    url = 'http://192.168.1.2:8082/downloads/10M.zip'
    main(url=url, thread=10, save_file='test.iso', buffer=4096)
