__author__ = 'zsh'


n=4
a=b=1
for i in range(3,n+1):
    a,b=b,(a+b)%20132013
print b