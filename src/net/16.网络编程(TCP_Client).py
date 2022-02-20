# coding=gb2312
#/usr/bin/env python

from time import ctime
from socket import *
    
HOST = 'localhost'
PORT = 21576
BUFSIZ = 1024
ADDR = (HOST, PORT)

def main():
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
        
    while True:
        data = raw_input('> ')
        if not data:
            break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data)        
    
    tcpCliSock.close()
    
    
if __name__ == '__main__':
    main()
    
    
    

