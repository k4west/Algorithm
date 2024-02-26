import sys
P = [[0] * 8 for _ in range(8)]
prev = i = 0
for k, p in enumerate(map(int, sys.stdin.readline().split()), 1):
    j = k - prev
    P[i][j], P[j][i] = p / 100, 1 - p / 100
    if j == 7:
        i += 1
        prev = k - i

tmp = []
for n in range(1, 9):
    if n % 2:
        a, b = (n + 1) % 4 + (n // 4) * 4, (n + 2) % 4 + (n // 4) * 4
        tmp.append(P[n - 1][n] * (P[n - 1][a] * P[a][b] + P[n - 1][b] * P[b][a]))
    else:
        a, b = (n) % 4 + ((n - 1) // 4) * 4, (n + 1) % 4 + ((n - 1) // 4) * 4
        tmp.append(P[n - 1][n - 2] * (P[n - 1][a] * P[a][b] + P[n - 1][b] * P[b][a]))

ans = []
for n in range(1, 9):
    if (n + 3) % 8 // 4: ans.append(tmp[n - 1] * sum(P[n - 1][i] * tmp[i] for i in range(4, 8)))
    else: ans.append(tmp[n - 1] * sum(P[n - 1][i] * tmp[i] for i in range(4)))
print(" ".join(map(lambda x: f"{x:.13f}", ans)))