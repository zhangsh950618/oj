__author__ = 'zsh'

a = 3
b = 2
s = '0123456789ABCDEF'
res = ''
while a:
    res = s[a % b] + res
    a /= b
print res
