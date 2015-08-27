__author__ = 'zsh'

from random import choice

aInt = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
bInt = choice(range(1, 11))
cInt = choice(range(1, 11))
dInt = choice(range(1, 11))

aStr = raw_input("Number are: %d, %d, %d, %d ! \n" % (aInt, bInt, cInt, dInt))

if eval(aStr) == 24:
    print("Right!")
else:
    print("Wrong!")
