import sys
import bisect
N, M = map(int, sys.stdin.readline().split())
names = [0]*N
powers = [0]*N
for i in range(N):
    names[i], power = sys.stdin.readline().split()
    powers[i] = int(power)
for _ in range(M):
    power = int(sys.stdin.readline())
    print(names[bisect.bisect_left(powers, power)])