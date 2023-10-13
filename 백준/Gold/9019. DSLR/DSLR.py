import sys
from collections import deque
input = sys.stdin.readline
li = []
for _ in range(int(input())):
    s, e = map(int, input().split())
    visited = [False]*10000
    q = deque([(s, "")])
    visited[s] = True
    while q:
        x, op = q.popleft()
        if x == e:
            li.append(op)
            break
        x0 = (x<<1)%10000
        if not visited[x0]:
            visited[x0] = True
            q.append((x0, op + "D"))
        x1 = (x-1)%10000
        if not visited[x1]:
            visited[x1] = True
            q.append((x1, op + "S"))
        x2 = (x*10)%10000 + x//1000
        if not visited[x2]:
            visited[x2] = True
            q.append((x2, op + "L"))
        x3 = x%10*1000 + x//10
        if not visited[x3]:
            visited[x3] = True
            q.append((x3, op + "R"))
print("\n".join(li))