import heapq
from sys import stdin
li = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n: heapq.heappush(li, n)
    else:
        if li: print(heapq.heappop(li))
        else: print(0)