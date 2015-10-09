# -*- coding:utf-8 -*-
import MySQLdb
import md5

__author__ = 'zsh'
import xlrd

filename = 'C:\Users\zsh\Documents\Private Files\OnlineJudge\名单.xlsx'
filename = unicode(filename, 'utf-8')
# 获取excel
xls = xlrd.open_workbook(filename)
# 获取sheet
sheet = xls.sheets()[0]

conn = MySQLdb.connect(host="localhost", user="root", passwd="Zsh950618", db="tsoj", charset="utf8")
cursor = conn.cursor()

sqlInsert = 'insert into user (userName, password, name,studentNumber, major, firstLogin, submitNumber, acceptNumber) values (%s,%s,%s,%s,%s,%s,%s,%s)'

m = md5.new()
# 循环遍历
print(sheet.nrows)
for i in range(sheet.nrows):
    id = sheet.cell(i, 0).value
    password = sheet.cell(i, 0).value
    m.update(str(password))
    name = sheet.cell(i, 1).value
    major = sheet.cell(i, 2).value
    args = (id, m.hexdigest(), name, id, major, 0, 0, 0)
    cursor.execute(sqlInsert, args)
conn.commit()
conn.close()
