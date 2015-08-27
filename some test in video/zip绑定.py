# coding=utf-8
__author__ = 'zsh'

numList = [1, 2, 3, 4]
fruitList = ["apple", "pear", "banana", "cheer"]
zipList = zip(fruitList, numList)
dictList = dict(zipList)

print(zipList, dictList)
print(dictList['apple'])
