def rd(n):
    return int(n) + int(n - int(n) >= 0.5)

a = open(0)
next(a)
li = list(map(int, a))
if li:
    N = len(li)
    n = rd(N*0.15)
    li.sort()
    level = rd(sum(li[n:N-n])/(N-2*n))
    print(level)
else: print(0)