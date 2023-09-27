import sys
def f(li, m):
    return sum([h-m for h in li if h > m])
N, M = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
s = 0
e = max(li)
while s!=e:
    m = (s+e)//2
    if M <= f(li, m):
        s = m
        if e-s == 1:
            break
    else:
        e = m
print(m) 