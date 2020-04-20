# -*- coding: GBK -*
# Author: Seay
# Blog :www.cnseay.com

import os,sys

def func_countfileline(filepath):
    num =0
    thefile=open(filepath, 'rb')
    while True:
        buffer = thefile.read(104857600)
        if not buffer:
            break
        num +=  buffer.count('\n')
    thefile.close()
    print '\t-- '+str(num+1)
    return num+1

def func_walks(path):
    line_count=0
    file_count=0
    for root, dirs, files in os.walk(path):
        for f in files:
            f = os.path.join(root, f)
            print f,
            file_count+=1
            line_count+=func_countfileline(f)
    return '\n\n�ļ�����'+str(file_count)+'\n������:'+str(line_count)
   
if __name__ == '__main__':    
    if len(sys.argv)>=3 and (sys.argv[1]=='-f' or sys.argv[1]=='-d'):
        if sys.argv[1]=='-f' and os.path.isfile(sys.argv[2]):
            print sys.argv[2],
            print '\n\n������: ' + str(func_countfileline(sys.argv[2]))
        elif sys.argv[1]=='-d' and os.path.exists(sys.argv[2]):
            print func_walks(sys.argv[2])
        else:
            print '-- �ļ�(��)'+sys.argv[2]+'������'
    elif len(sys.argv)==1:
        print func_walks(os.getcwd())
    else:
        print '-- ����˵�� ��'
        print '    1. '+sys.argv[0]+ ' -f' +' filename \tͳ��ָ���ļ�����'
        print '    2. '+sys.argv[0]+ ' -d' +' directory \tͳ��ָ��Ŀ¼(������Ŀ¼)�µ��ļ�������'
        print '    3. '+sys.argv[0]+ ' \tͳ�Ƶ�ǰĿ¼(������Ŀ¼)�µ��ļ�������'