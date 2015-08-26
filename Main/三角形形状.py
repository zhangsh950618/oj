#encoding=utf-8
__author__ = 'zsh'


a=3
b=4
c=5

L=[a,b,c]
L.sort()
if L[0] + L[1] <= L[2]:
    print 'W'
elif pow(L[0],2) + pow(L[1],2)==pow(L[2],2):
    print 'Z'
elif pow(L[0],2) + pow(L[1],2)>pow(L[2],2):
    print 'R'
else:
    print 'D'


