#!/usr/bin/env python
# coding=utf-8

import sys
import pymysql
pymysql.install_as_MySQLdb()   # 可选：为了兼容旧代码
import MySQLdb
import sys
import os
sys.path.append(os.getcwd() + '/src')
from util.ConfigUtil import ConfigUtil
ConfigUtil = ConfigUtil()

def connMySQL():
    config = ConfigUtil.get_config('conf/dev.txt')
    conn = pymysql.connect(host=config['mysql_host'], port=int(config['mysql_port']), 
                           user=config['mysql_user'], passwd=config['mysql_password'], db=config['mysql_database'])
    #conn = MySQLdb.connect(user='root', passwd='123456', host='localhost',db='test')
    cursor = conn.cursor()
    sql = 'select * from user limit 10'
    cursor.execute(sql)

    row = cursor.fetchone()
    print(row)

    list = cursor.fetchall()
    print(list)
    #for i in list:
    #    print(i)
    #    for j in i:
    #        print(j)

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    connMySQL()
    
    
    
    
    
    
    



