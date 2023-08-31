import sys
from itertools import combinations
a, b = map(int, sys.stdin.readline().split())
if a == b:
    print("{:.3f}".format(round(1-(10-a)/153, 3)))
else:
    li = list(range(1,11))*2
    li.remove(a)
    li.remove(b)
    a = (a+b)%10
    cb = combinations(li, 2)
    s = 0
    for c in cb:
        if c[0] != c[1] and sum(c)%10 < a:
            s += 1
    print("{:.3f}".format(round(s/153, 3)))