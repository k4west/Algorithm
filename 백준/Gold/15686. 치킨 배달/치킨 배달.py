from sys import stdin
from itertools import combinations
input = stdin.readline

N, M = map(int, input().split())
house, chicken, select = [], [], []
ans, nc = 10000, 0
for i in range(N):
    for j, hc in enumerate(input().rstrip().split()):
        if hc == '1': 
            house.append((i, j))
        if hc == '2':
            chicken.append((i, j))
            nc += 1

for select in combinations(chicken, M):
    s_dist = 0
    for r1, c1 in house:
        dist = 100
        for r2, c2 in select:
            tmp = abs(r2-r1) + abs(c2-c1)
            if tmp < dist: dist = tmp
        s_dist += dist
    if s_dist < ans: ans = s_dist

print(ans)