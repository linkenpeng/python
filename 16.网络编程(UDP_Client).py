# coding=gb2312
#/usr/bin/env python

from time import ctime
from socket import *

HOST = 'localhost'
PORT = 21576
BUFSIZ = 1024
ADDR = (HOST, PORT)

def main():
    udpCliSock = socket(AF_INET, SOCK_DGRAM)
            
    while True:
        data = raw_input('> ')
        if not data:
            break
        udpCliSock.sendto(data, ADDR)
        data, addr = udpCliSock.recvfrom(BUFSIZ)
        if not data:
            break
        print(data)     
    
    udpCliSock.close()    
    
if __name__ == '__main__':
    main()
    
    
    

