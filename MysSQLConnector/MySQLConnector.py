# -*- coding:utf-8 -*-
__author__ = 'zsh'

import MySQLdb


# 链接mysql
connOld = MySQLdb.connect(host="localhost", user="root", passwd="Zsh950618", db="nuistojv2", charset="utf8")
connProblem = MySQLdb.connect(host="172.16.102.91", user="zsh", passwd="Zsh950618", db="tsoj", charset="utf8")
cursorOld = connOld.cursor()
cursorProblem = connProblem.cursor()

# 查询

sqlSearch = "select * from problem"

cursorOld.execute(sqlSearch)



# 获取结果集合
problems = cursorOld.fetchall()

insertIntoProblem = "INSERT INTO problem (title,description,input,output,sampleInput,sampleOutput,timeLimit,memoryLimit,difficultyId) \
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

for problem in problems:
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
    args = (title, description, input, output, sampleInput, sampleOutput, timeLimit, memoryLimit, 1)
    cursorProblem.execute(insertIntoProblem, args)
connProblem.commit()

insertIntoExercise = "INSERT INTO exercise_problem (problemId, submitNumber, acceptNumber) \
            VALUES (%s,%s,%s)"
for problemId in range(1003, 1254):
    print(problemId)
    args = (problemId, 0, 0)
    cursorProblem.execute(insertIntoExercise,args)
connProblem.commit()
