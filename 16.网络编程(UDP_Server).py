# coding=gb2312
#/usr/bin/env python

from time import ctime
from socket import *

HOST = 'localhost'
PORT = 21576
BUFSIZ = 1024
ADDR = (HOST, PORT)

def main():
    udpSerSock = socket(AF_INET, SOCK_DGRAM)
    udpSerSock.bind(ADDR)
        
    while True:
        print('warting for message...')
        data,addr = udpSerSock.recvfrom(BUFSIZ)
        udpSerSock.sendto('[%s] %s' % (ctime(),data), addr)
        print(data,'...received from and returned to:', addr)
    
    udpSerSock.close()    
    
if __name__ == '__main__':
    main()
    
    
    

