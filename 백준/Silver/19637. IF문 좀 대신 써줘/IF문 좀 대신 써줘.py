import sys
import bisect
N, M = map(int, sys.stdin.readline().split())

d = {}
for _ in range(N):
    name, power = sys.stdin.readline().split()
    if int(power) not in d:
        d[int(power)] = name
powers = list(d.keys())

for _ in range(M):
    power = int(sys.stdin.readline())
    print(d[powers[bisect.bisect_left(powers, power)]])