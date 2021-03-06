# -*- coding:utf-8 -*-
import MySQLdb
import hashlib
import base64
from random import choice
import string
import xlrd
import xlwt
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'zsh'

filename = 'C:\Users\zsh\Documents\Private Files\NUISTOJ\程序设计大赛\导入表.xlsx'
filename = unicode(filename, 'utf-8')
# 获取excel
xls = xlrd.open_workbook(filename)
# 获取sheet
sheet = xls.sheets()[0]

conn = MySQLdb.connect(host="172.16.102.91", user="zsh", passwd="Zsh950618", db="tsoj", charset="utf8")
cursor = conn.cursor()

sqlInsertUser = 'insert into user (id , userName, password, name,major, studentNumber, firstLogin, submitNumber, acceptNumber) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
sqlInsertContest = 'insert into contest_user (userId , contestId, submitNumber ,acceptNumber,classroom , place) values (%s,%s,%s,%s,%s,%s)'
sqlClear = 'SET foreign_key_checks=0;\
            truncate table tsoj.user;\
            truncate table tsoj.contest_user;\
            SET foreign_key_checks=1;'
cursor.execute(sqlClear)
# 循环遍历
print(sheet.nrows)
for i in range(1, sheet.nrows):
    userId = i
    userName = sheet.cell(i, 0).value
    userName = str(userName)
    password = sheet.cell(i, 1).value
    password = str(password)
    m2 = hashlib.md5()
    m2.update(password)
    studentName = sheet.cell(i, 2).value
    major = sheet.cell(i, 3).value
    studentNumber = sheet.cell(i, 4).value
    classroom = sheet.cell(i, 5).value
    classroom = base64.b64encode(classroom)
    place = sheet.cell(i, 6).value
    place = base64.b64encode(place)
    print(m2.hexdigest())
    userArgs = (userId, userName, m2.hexdigest(), studentName, major, studentNumber, 1, 0, 0)
    contestArgs = (userId, 35, 0, 0, classroom, place)
    cursor.execute(sqlInsertUser, userArgs)
    cursor.execute(sqlInsertContest, contestArgs)
conn.commit()
conn.close()
