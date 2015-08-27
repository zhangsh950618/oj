# coding=utf-8
from collections import Counter

__author__ = 'zsh'


# 统计一个字符串中出现的个数


aStr = "handkerchief'sKJLKZCBl:JKL"
# aDict = {}

# for i in aStr:
# """ D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D """
# 如果不存在就初始化为0
# aDict[i] += 1
# print(aDict)

print(Counter(aStr))
