__author__ = 'zsh'



s="202.115.32.24"
S=s.split('.')

def judge():
    if len(S) != 4:
        return False
    for ss in S:
        try:
            if int(ss) not in range(0,256):
                return  False
        except:
            return False
    return True


print 'Yes' if judge() else 'No'




