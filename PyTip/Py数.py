__author__ = 'zsh'


n=2992
def tran(n,number):
    sum=0
    while number:
        sum+=number%n
        number/=n
    return sum

print 'Yes' if tran(10,n)==tran(12,n)==tran(16,n) else 'No'



