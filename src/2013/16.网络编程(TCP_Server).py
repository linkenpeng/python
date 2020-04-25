# coding=gb2312
#/usr/bin/env python

from time import ctime
from socket import *
    
HOST = 'localhost'
PORT = 21576
BUFSIZ = 1024
ADDR = (HOST, PORT)

def main():
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)
        
    while True:
        print('warting for connection...')
        tcpCliSock,addr = tcpSerSock.accept()
        print('...connencted from:', addr)
        
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            tcpCliSock.send('[%s] %s' % (ctime(),data))
        tcpCliSock.close()
    
    tcpSerSock.close()
    
    
if __name__ == '__main__':
    main()
    
    
    

