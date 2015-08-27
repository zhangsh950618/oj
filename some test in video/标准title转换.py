# coding=utf-8

__author__ = 'zsh'
# 输入一行字符串转换成标准title
# 每个单词的首字母大写并且中间只有一个空行

aStr = raw_input("please input a string \n")

aStr = aStr.title()
aList = aStr.split()
aStrNew = " ".join(aList)

print(aStrNew)
