# coding=utf-8
__author__ = 'zsh'

# 去掉一个最高分去掉一个最低分计算平均值
aList = []
while len(aList) < 3:
    aStr = raw_input("please input more than three numbers\n");
    aList = [int(item) for item in aStr.split()]
aList.sort()
print(aList)
aList = aList[1:-1]
print("the average is %.2f \n" % (float(sum(aList)) / len(aList)))
