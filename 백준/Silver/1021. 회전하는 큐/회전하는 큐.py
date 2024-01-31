import sys

input = lambda: map(int, sys.stdin.readline().split())
N, M = input()
q = list(range(1, N + 1))
ans = t = 0

for a in input():
    x = q.index(a)
    y = min((x - t) % N, (t - x) % N)
    q.pop(x)
    N -= 1
    ans += y
    t = x

print(ans)