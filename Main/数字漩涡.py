__author__ = 'zsh'



n=4
array=[[0 for x in range(n)] for y in range(n)]
i=0
j=0
number=1
while number <= pow(n,2):
    for row in range(n):
        array[i][j]=number
        j+=1
        print j

for i in range(n):
    for j in range(n-1):
        print array[i][j],
    print array[i][j]
