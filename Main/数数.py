__author__ = 'zsh'


n=10

sum=0
for i in range(0,n+1):
    while i:
        if i % 10 ==1:
            sum +=1
        i/=10
print sum