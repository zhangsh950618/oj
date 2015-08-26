__author__ = 'zsh'





a="cagy"
b=3
res=''
for char in a:
    res+=chr((ord(char)+b-97)%26+97)
print res