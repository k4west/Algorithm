import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque([n])
c = [0] * (n+1)
while q:
    p = q.popleft()
    if p == 1:
        print(c[1])
        break
    if p % 3 == 0 and not c[p//3]:
        c[p//3] = c[p]+1
        q.append(p//3)
    if p % 2 == 0 and not c[p//2]:
        c[p//2] = c[p]+1
        q.append(p//2)
    if not c[p-1]:
        c[p-1] = c[p]+1
        q.append(p-1)