# coding=utf-8

import os

__author__ = 'zsh'

inpath = 'C:\Users\zsh\Documents\Private Files\OnlineJudge\蓝桥杯题库\蓝桥杯题库'
# print(inpath)


# 中文重新编码
uipath = inpath.decode('utf-8')
for list_name in os.walk(uipath):
    print(list_name)


