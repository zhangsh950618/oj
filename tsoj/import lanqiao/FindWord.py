# coding=utf-8

import os
from docx import Document
__author__ = 'zsh'

inpath = 'C:\Users\zsh\Documents\Private Files\OnlineJudge\蓝桥杯题库\蓝桥杯题库'
# print(inpath)




# 中文重新编码
uipath = inpath.decode('utf-8')
for partent, dirnames, filenames in os.walk(uipath):
    for filename in filenames:
        # print(filename)6
        if filename.endswith('.doc') or filename.endswith('.docx'):
            print(filename)
            fullname = os.path.join(partent, filename)
            print(fullname)
            document = Document(fullname)



