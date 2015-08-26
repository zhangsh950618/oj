__author__ = 'zsh'


N=5
K=2
res=1
for i in range(1,N+1):
    res*=i
    while res%10 == 0:
        res /= 10
    res %= 1000000000

while res%10 == 0:
    res /= 10
res %= 1000000000
res=str(res)



