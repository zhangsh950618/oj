# -*- coding:utf-8 -*-
import os
import re
import MySQLdb
import datetime

__author__ = 'zsh'




# 链接mysql
connOld = MySQLdb.connect(host="localhost", user="root", passwd="Zsh950618", db="nuistojv2", charset="utf8")
connProblem = MySQLdb.connect(host="172.16.102.91", user="zsh", passwd="Zsh950618", db="tsoj", charset="utf8")
cursorOld = connOld.cursor()
cursorProblem = connProblem.cursor()

# 查询

sqlSearch = "select * from problem"

cursorOld.execute(sqlSearch)
connOld.close()
rootdir = "C:\Users\zsh\Desktop\problem"
for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名
    for dir in dirnames:
        os.rename(os.path.join(rootdir, dir), os.path.join(rootdir, str(int(dir) + 1000)))
    for filename in filenames:  # 输出文件信息
        if filename != 'in.1' and filename != 'out.1':
            print('delete file:', os.path.join(parent, filename))
            os.remove(os.path.join(parent, filename))
            # print "the full name of the file is:" + os.path.join(parent, filename)  # 输出文件路径信息
for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:  # 输出文件信息
        if filename == 'in.1':
            os.rename(os.path.join(parent, 'in.1'), os.path.join(parent, '1.in'))
        if filename == 'out.1':
            os.rename(os.path.join(parent, 'out.1'), os.path.join(parent, '1.ans'))


# 获取结果集合
problems = cursorOld.fetchall()

insertIntoProblem = "INSERT INTO problem (title,description,input,output,sampleInput,sampleOutput,timeLimit,memoryLimit,difficultyId,submitTime) \
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"


# 对有效题目计数
count = 0
# 获取当前时间
now = datetime.datetime.now()
sqlClear = 'SET foreign_key_checks=0;\
            truncate table tsoj.problem;\
            truncate table tsoj.exercise_problem;\
            ALTER TABLE tsoj.problem AUTO_INCREMENT = 1001;\
            SET foreign_key_checks=0;'
cursorProblem.execute(sqlClear)

tihuan = re.compile('<.*?>|\s+')
duanluokaishi = re.compile('<p>')
duanluojieshu = re.compile('</p>')
xiaoyu = re.compile('&lt;')
dayu = re.compile('&gt;')
zuoyinhao = re.compile('&ldquo;')
youyinhao = re.compile('&rdquo;')
xiaoyudengyu = re.compile('&le;')
dayudengyu = re.compile('&ge;')
shenglve = re.compile('&hellip;')


def fuctiontihuan(x):
    # x = xiaoyu.sub('lt;&amp;', x)
    # x = duanluokaishi.sub('&lt;p&gt;', x)
    # x = duanluojieshu.sub('&lt;/p&gt;', x)
    x = tihuan.sub('', x)
    # x = x.replace(' ', '')
    # x = x.replace('\n', '')
    # x = x.strip()

    # print(x)

    # x = dayu.sub('>', x)
    # x = zuoyinhao.sub('"', x)
    # x = youyinhao.sub('"', x)
    # x = xiaoyudengyu.sub('<=', x)
    # x = dayudengyu.sub('>=', x)
    # x = shenglve.sub('...', x)
    # print x
    return x


for problem in problems:
    pid = problem[1]
    timeLimit = problem[12]
    memoryLimit = problem[13]
    problem = problem[3:9]
    problem = map(fuctiontihuan, problem)
    # for i in problem:
    #     print(i)
    title = problem[0]
    description = problem[1]
    input = problem[2]
    output = problem[3]
    sampleInput = problem[4][:100:]
    sampleOutput = problem[5][:100:]
    if description != '' and title != '':
        args = (title, description, input, output, sampleInput, sampleOutput, timeLimit, memoryLimit, 1,
                now + datetime.timedelta(seconds=count))
        cursorProblem.execute(insertIntoProblem, args)
        count += 1
        # 对于测试数据转换格式
        print(os.path.join(rootdir, str(pid)), 'to' , os.path.join(rootdir, str(1000+count)))
        os.rename(os.path.join(rootdir, str(pid + 1000)), os.path.join(rootdir, str(1000+count)))
connProblem.commit()

print('all problem is ', count)

# 对于exercise表绑定

insertIntoExercise = "INSERT INTO exercise_problem (problemId, submitNumber, acceptNumber) \
            VALUES (%s,%s,%s)"
for problemId in range(1001, 1001 + count):
    # print(problemId)
    args = (problemId, 0, 0)
    cursorProblem.execute(insertIntoExercise, args)
connProblem.commit()
connProblem.close()
