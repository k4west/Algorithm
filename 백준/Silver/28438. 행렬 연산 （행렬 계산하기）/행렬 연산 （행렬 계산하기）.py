import sys
input = lambda: map(int, sys.stdin.readline().split())
n, m, q = input()
row = [0 for _ in range(n)]
col = [0 for _ in range(m)]
for _ in range(q):
    op, k, v = input()
    if op == 1: row[k - 1] += v
    if op == 2: col[k - 1] += v
print("\n".join(((" ".join(map(str, (row[i] + col[j] for j in range(m))))) for i in range(n))))