#!/usr/bin/env python
# coding=utf-8

import sys
import MySQLdb
conn = MySQLdb.connect(user='root', passwd='123456', host='localhost',db='aifaxian')
cursor = conn.cursor()
sql = 'select * from uchome_space limit 10'
cursor.execute(sql)

#row = cursor.fetchone()
#print(row) 

list = cursor.fetchall()
print(list)
#for i in list:
#    print(i)
#    for j in i:
#        print(j)

conn.commit()
cursor.close()
conn.close()
    
    
    
    
    
    
    



