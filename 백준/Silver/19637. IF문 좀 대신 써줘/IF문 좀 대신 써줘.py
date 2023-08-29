import sys
N, M = map(int, sys.stdin.readline().split())

d = {}
for _ in range(N):
    name, power = sys.stdin.readline().split()
    if int(power) not in d:
        d[int(power)] = name
powers = tuple(d.keys())

for _ in range(M):
    s, e = 0 , len(powers)-1
    power = int(sys.stdin.readline())
    while s!=e:
        m = (s+e)//2
        p = powers[m]
        if power <= p:
            e = m
        else:
            s = m+1
    print(d[powers[s]])