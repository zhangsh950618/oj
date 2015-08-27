# coding=utf-8
from random import choice

__author__ = 'zsh'

# 输入几个数字然后从这几个数字里面随机100000次查看每个数字的出现的个数


# 获取用户输入的内容
aStr = raw_input("please input some numbers \n")
aList = [int(item) for item in aStr.split()]
aNumList = [choice(aList) for i in range(1000000)]

bNumList = [(i, aNumList.count(i)) for i in aList]
for x, y in bNumList:
    print("%d = > %d" % (x, y))
