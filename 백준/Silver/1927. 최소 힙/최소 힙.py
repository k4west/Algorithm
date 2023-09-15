import heapq
def f(a):
    next(a)
    li, t = [], []
    for n in a:
        if n=="0\n":
            if li: t.append(str(heapq.heappop(li)))
            else: t.append("0")
        else:
            heapq.heappush(li, int(n))
    print(*t, sep="\n")
a = open(0)
f(a)