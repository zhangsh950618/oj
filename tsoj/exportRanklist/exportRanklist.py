# -*- coding:utf-8 -*-
import MySQLdb
import datetime
import time
import base64
from xlwt import *

__author__ = 'zsh'
conn = MySQLdb.connect(host="localhost", user="root", passwd="Zsh950618", db="tsoj", charset="utf8")
cursor = conn.cursor()

w = Workbook()
ws = w.add_sheet(u'第六届程序设计大赛排名')
sql_select_solutions = "SELECT * FROM tsoj.solution WHERE problemId >= 1238 AND problemId <= 1244\
                        AND userId = %s AND submitTime BETWEEN '2015-11-07 08:30:00' AND\
                         '2015-11-07 12:30:00'"
sql_select_user = "SELECT * FROM tsoj.user WHERE id = %s"
sql_select_sourcecode = 'SELECT code FROM source_code where id = %s'
ws.write(0, 0, u'姓名')
ws.write(0, 1, u'学号')
ws.write(0, 2, u'专业')
ws.write(0, 3, u'通过数')
ws.write(0, 4, u'报名参军')
ws.write(0, 5, u'鼓舞士气')
ws.write(0, 6, u'探测敌情')
ws.write(0, 7, u'计算距离')
ws.write(0, 8, u'寻找内奸')
ws.write(0, 9, u'运输装备')
ws.write(0, 10, u'火烧连营')
ws.write(0, 11, u'总用时')
ws.write(0, 12, u'报名参军AC代码')
ws.write(0, 13, u'鼓舞士气AC代码')
ws.write(0, 14, u'探测敌情AC代码')
ws.write(0, 15, u'计算距离AC代码')
ws.write(0, 16, u'寻找内奸AC代码')
ws.write(0, 17, u'运输装备AC代码')
ws.write(0, 18, u'火烧连营AC代码')
start_time = datetime.datetime.strptime('2015-11-07 08:30:00', '%Y-%m-%d %H:%M:%S')
print start_time
for i in range(287, 288):
    cursor.execute(sql_select_solutions, (i,))
    solutions = cursor.fetchall()
    problem = [0] * 7
    penalty_time = [0] * 7
    early_time = '2015-11-07 12:30:00'
    mintime = [early_time] * 7
    final_time = [0] * 7
    source_code = [''] * 7
    for solution in solutions:
        print(solution)
        if solution[7] == 1:
            # print(str(solution[4]))
            if str(solution[4]) < mintime[solution[2] - 1238]:
                mintime[solution[2] - 1238] = str(solution[4])
                cursor.execute(sql_select_sourcecode, (solution[0],))
                source_code[solution[2] - 1238] = base64.b64decode(cursor.fetchall()[0][0])
            problem[solution[2] - 1238] = 1
    print(problem)
    count = sum(problem)
    # print(mintime)
    # print(datetime.datetime.strptime(mintime[0], '%Y-%m-%d %H:%M:%S'))
    for solution in solutions:
        if solution[7] != 1 and mintime[solution[2] - 1238] > str(solution[4]):
            penalty_time[solution[2] - 1238] += 1
    # print(penalty_time)
    cursor.execute(sql_select_user, (i,))
    user = cursor.fetchall()[0]
    print(user)
    tot_time = 0
    for j in range(7):
        if problem[j] == 1:
            final_time = (datetime.datetime.strptime(mintime[j], '%Y-%m-%d %H:%M:%S') - start_time).seconds + \
                         penalty_time[j] * 1200
        else:
            final_time = penalty_time[j] * 1200
        tot_time += final_time
        if final_time != 0:
            final_time_towrite = time.strftime("%H:%M:%S", time.gmtime(final_time))
            if penalty_time[j] != 0:
                ws.write(i, j + 4, final_time_towrite + '(-' + str(penalty_time[j]) + ')')
            else:
                ws.write(i, j + 4, final_time_towrite)
        ws.write(i, j + 12, source_code[j].decode('utf-8'))
    ws.write(i, 11, time.strftime("%H:%M:%S", time.gmtime(tot_time)))
    ws.write(i, 0, user[3])
    ws.write(i, 3, count)
    ws.write(i, 1, user[5])
    ws.write(i, 2, user[4])
w.save(u"第六届程序设计大赛排名.xls")
