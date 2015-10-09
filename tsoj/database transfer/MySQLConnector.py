# -*- coding:utf-8 -*-
import os
import MySQLdb
import datetime
__author__ = 'zsh'




# 链接mysql
connOld = MySQLdb.connect(host="localhost", user="root", passwd="Zsh950618", db="nuistojv2", charset="utf8")
connProblem = MySQLdb.connect(host="localhost", user="root", passwd="Zsh950618", db="tsoj", charset="utf8")
cursorOld = connOld.cursor()
cursorProblem = connProblem.cursor()

# 查询

sqlSearch = "select * from problem"

cursorOld.execute(sqlSearch)
connOld.close()
rootdir = "C:\Users\zsh\Desktop\problem"


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
for problem in problems:
    pid = problem[1]
    title = problem[3]
    # title.decode('utf-8')
    # print title, type(title)
    description = problem[4]
    # print description, type(description)
    input = problem[5]
    # print input, type(input)
    output = problem[6]
    # print output, type(output)
    sampleInput = problem[7][:100:]
    # print sampleInput, type(sampleInput)
    sampleOutput = problem[8][:100:]
    # print sampleOutput, type(sampleOutput)
    timeLimit = problem[12]
    # print timeLimit, type(timeLimit)
    memoryLimit = problem[13]
    # print memoryLimit, type(memoryLimit)
    if output != '':
        args = (title, description, input, output, sampleInput, sampleOutput, timeLimit, memoryLimit, 1,
                now + datetime.timedelta(seconds=count))
        cursorProblem.execute(insertIntoProblem, args)
        count += 1
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
