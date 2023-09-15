import heapq
from sys import stdin
def f(a):
    next(a)
    li, t = [], []
    for n in a:
        n = int(n)
        if n: heapq.heappush(li, n)
        else:
            if li: t.append(str(heapq.heappop(li)))
            else: t.append("0")
    print(*t, sep="\n")
a = open(0)
f(a)