import sys
from collections import Counter
if __name__=="__main__":
    def f(d):
        s = 0
        e = max(d)
        while s<=e:
            m = (s+e)//2
            if M <= sum(((h-m)*i for h, i in d.items() if h > m)):
                s = m+1
            else:
                e = m-1
        print(e)
    N, M = map(int, sys.stdin.readline().split())
    d = Counter(map(int, sys.stdin.read().split()))
    f(d)