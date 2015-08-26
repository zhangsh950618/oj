__author__ = 'zsh'





n=3
L=[0,1]
for i in range(2,n+1):
    L.append(L[-1]+L[-2])
print L[n]
