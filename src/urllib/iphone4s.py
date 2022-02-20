#!/usr/bin/python
 
import urllib.request
import sys
import time
 
def alarm():
    while True:
        sys.stdout.write('\a')
        sys.stdout.flush()
 
def poll():
    count=0;
    while True:
        count = count + 1
        now = time.localtime( time.time() )
        print('%02d:%02d:%02d %d' % (now.tm_hour, now.tm_min, now.tm_sec, count))
        try:
            urllib.request.urlopen('http://store.apple.com/hk-zh/browse/home/shop_iphone/family/iphone/iphone4s')
            alarm()
        except urllib.request.HTTPError as error:
            pass
            #print error
 
        try:
            iphone4 = urllib.request.urlopen( 'http://store.apple.com/hk-zh/browse/home/shop_iphone/family/iphone/iphone4' )
            html = ''.join( iphone4.readlines() )
            if html.find( 'iPhone 4S' ) != -1 :
                alarm()
        except:
            pass
 
        #time.sleep(1)
 
if __name__ == '__main__':
    poll()