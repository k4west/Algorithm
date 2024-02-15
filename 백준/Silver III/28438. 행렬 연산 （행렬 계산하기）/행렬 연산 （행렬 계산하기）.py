import sys
input = lambda: map(int, sys.stdin.readline().split())
n, m, q = input()
metrix = [0 for _ in range(n * m)]
row = [0 for _ in range(n)]
col = [0 for _ in range(m)]
for _ in range(q):
    op, k, v = input()
    if op == 1: row[k - 1] += v
    if op == 2: col[k - 1] += v
for i in range(n):
    for j in range(m): metrix[m * i + j] += row[i] + col[j]
for i in range(n): print(" ".join(map(str, metrix[i * m : (i + 1) * m])))