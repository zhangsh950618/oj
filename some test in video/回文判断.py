# coding=utf-8
__author__ = 'zsh'


# 判断用户输入的字符串是否为回文字符串，注意处理输入的空白

aStr = raw_input("please input a string \n")
# 处理用户输入的开始的空白
aStr = aStr.strip()

if aStr == aStr[::-1]:
    print("%s  是回文" % aStr)
else:
    print("%s 不是回文" % aStr)
