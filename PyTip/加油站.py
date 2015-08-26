__author__ = 'zsh'

limit=[1,2,3,4,5,6]
cost=[1,2,3,4,5,6]
n=6
def judge(num):
    return False
for i in range(0,n,):
    if judge(i):
        print i
        exit(0)
print -1