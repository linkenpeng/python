# -*- coding: utf-8 -*-
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
    print('\t-- '+str(num+1))
    return num+1

def func_walks(path):
    line_count=0
    file_count=0
    for root, dirs, files in os.walk(path):
        for f in files:
            f = os.path.join(root, f)
            print(f),
            file_count+=1
            line_count+=func_countfileline(f)
    return '\n\n文件数：'+str(file_count)+'\n总行数:'+str(line_count)
   
if __name__ == '__main__':    
    if len(sys.argv)>=3 and (sys.argv[1]=='-f' or sys.argv[1]=='-d'):
        if sys.argv[1]=='-f' and os.path.isfile(sys.argv[2]):
            print(sys.argv[2]),
            print('\n\n总行数: ' + str(func_countfileline(sys.argv[2])))
        elif sys.argv[1]=='-d' and os.path.exists(sys.argv[2]):
            print(func_walks(sys.argv[2]))
        else:
            print('-- 文件(夹)'+sys.argv[2]+'不存在')
    elif len(sys.argv)==1:
        print(func_walks(os.getcwd()))
    else:
        print('-- 参数说明 ：')
        print('    1. '+sys.argv[0]+ ' -f' +' filename \t统计指定文件行数')
        print('    2. '+sys.argv[0]+ ' -d' +' directory \t统计指定目录(包括子目录)下的文件总行数')
        print('    3. '+sys.argv[0]+ ' \t统计当前目录(包括子目录)下的文件总行数')