# -*- coding:utf-8 -*-
import time, datetime
__author__ = 'zsh'

# print(time.time())
# print time.localtime(time.time())
d1 = datetime.datetime.now()
print(d1)
d3 = d1 + datetime.timedelta(seconds=10)
