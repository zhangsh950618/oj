# -*- coding:utf-8 -*-
__author__ = 'zsh'

import MySQLdb


# 链接mysql
conn = MySQLdb.connect(host="localhost", user="root", passwd="Zsh950618", db="nuistojv2", charset="utf8")
cursor = conn.cursor()



# 查询

sql = "select * from manageruser"

cursor.execute(sql)


#获取结果集合
cds=cursor.fetchall()
print cds







