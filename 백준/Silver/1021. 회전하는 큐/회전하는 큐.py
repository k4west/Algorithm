import sys
from collections import deque

input = lambda: map(int, sys.stdin.readline().split())
N, M = input()
q = deque(range(1, N + 1))
ans = 0

for i in input():
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if (n := q.index(i)) < (N) / 2:
                while q[0] != i:
                    q.append(q.popleft())
                    ans += 1
            else:
                while q[0] != i:
                    q.appendleft(q.pop())
                    ans += 1
    N -= 1

print(ans)