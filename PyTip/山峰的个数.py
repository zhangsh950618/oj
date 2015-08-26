__author__ = 'zsh'


h=[0.9,1.2,1.22,1.1,1.6,0.99]

print len([hill for hill in range(1,len(h)) if h[hill] > h[hill - 1] and h[hill] > h[hill +1]])