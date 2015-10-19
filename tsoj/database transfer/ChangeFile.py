# -*- coding:utf-8 -*-
import os
import os.path
__author__ = 'zsh'

rootdir = "C:\Users\zsh\Desktop\problem"  # 指明被遍历的文件夹

for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名
    for filename in filenames:  # 输出文件信息
        if filename != 'in.1' and filename != 'out.1':
            print('delete file:', os.path.join(parent, filename))
            os.remove(os.path.join(parent, filename))
            # print "the full name of the file is:" + os.path.join(parent, filename)  # 输出文件路径信息

