# coding=utf-8

import ThreadedWorker
from queue import Queue
 
urls_to_process = ["http://facebook.com", "http://pypix.com"]
 
work_queue = Queue()
result_queue = Queue()
 
def process_url(url):
    # TODO: Do some work with the url
    return url
 
def main():
    # spawn a pool of threads, and pass them queue instance 
    for i in range(5):
        t = ThreadedWorker(work_queue, result_queue, work_func=process_url)
        t.setDaemon(True)
        t.start()
 
    # populate queue with data   
    for url in urls_to_process:
        work_queue.put(url)
 
    # wait on the queue until everything has been processed     
    work_queue.join()
 
    # print results
    print(repr(result_queue))
 
main()