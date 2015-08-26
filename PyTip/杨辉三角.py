__author__ = 'zsh'

n=4

array = [[0 for x in range(n)]for y in range(n)]



for i in range(n):
    for j in range(n-1):
        print array[i][j],
    print array[i][j]