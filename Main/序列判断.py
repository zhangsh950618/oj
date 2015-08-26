__author__ = 'zsh'



L=[1,2,3,4,5,6,7,8]
print L==sorted(L) and 'UP' or L==(sorted(L)[::-1]) and 'DOWN' or 'WRONG'
