__author__ = 'zsh'


w=[2,5,11]
n=9
a={0:1}
for i in range(1,n+1,1):
    ok=False
    for ww in w:
        if i-ww >= 0 and a[i-ww]==1:
            a[i]=1
            ok=True
            break
    if ok==False:
        a[i]=0
print 'Yes'if a[n]==1 else 'No'





