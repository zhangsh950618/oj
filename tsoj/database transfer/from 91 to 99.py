# -*- coding:utf-8 -*-
__author__ = 'zsh'
import MySQLdb


connlocal = MySQLdb.connect(host="172.16.102.91", user="zsh", passwd="Zsh950618", db="tsoj", charset="utf8")
conn91 = MySQLdb.connect(host="localhost", user="root", passwd="Zsh950618", db="tsoj", charset="utf8")

cursor91 = conn91.cursor()
cursorlocal = connlocal.cursor()


sqlSearchProblem = "select * from problem"
sqlSearchExercise = "select * from exercise_problem"
sqlInsertProblem = "insert into problem values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sqlInsertExercise = "insert into exercise_problem values(%s,%s,%s,%s)"
sqlClear = 'SET foreign_key_checks=0;\
            truncate table tsoj.problem;\
            truncate table tsoj.exercise_problem;\
            ALTER TABLE tsoj.problem AUTO_INCREMENT = 1001;\
            SET foreign_key_checks=1;'
cursor91.execute(sqlSearchProblem)
cursorlocal.execute(sqlClear)


problems = cursor91.fetchall()
for problem in problems:
    cursorlocal.execute(sqlInsertProblem, problem)

cursor91.execute(sqlSearchExercise)
exercises = cursor91.fetchall()
for exercise in exercises:
    cursorlocal.execute(sqlInsertExercise, exercise)
connlocal.commit()

