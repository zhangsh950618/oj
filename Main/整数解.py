__author__ = 'zsh'


a=9
b=15
def judge():
    for x in range(-10000,10001,1):
        for y in range(-10000,10001,1):
            if x+y==a and x*y==b:
                return 'YES'
    return 'NO'
print judge()
