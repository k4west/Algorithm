from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

ans = []
hq = []
N = int(input())
X = [int(input()) for _ in range(N)]

for x in X:
    if x:
        heappush(hq, x)
    elif hq:
        ans.append(heappop(hq))
    else:
        ans.append(0)

print("\n".join(map(str, ans)))
