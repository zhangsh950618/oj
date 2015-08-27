# coding=utf-8
__author__ = 'zsh'
# 题目要求：
# 提示输入一个数字，输出这笔钱等于多少张50圆，10圆,5圆和1圆（张数最少）
aNumStr = raw_input("please input X yuan :\n")
aNum = int(aNumStr)
tmpNum = aNum
fiftyNum, tmpNum = divmod(tmpNum, 50)
tenNum, tmpNum = divmod(tmpNum, 10)
fiveNum, oneNum = divmod(tmpNum, 5)
print("%d yuan = %d 50 yuan, %d 10 yuan, %d 5 yuan, %d 1 yuan" % (aNum, fiftyNum, tenNum, fiveNum, oneNum))
