__author__ = 'zsh'


L=[2,-3,3,50]


sum=0
res=-1<<20
for l in L:
    sum+=l
    res=max(res,sum)
    if sum < 0:
        sum=0
print res