import sys
input = sys.stdin.readline

N = int(input())
d = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
bomb = []
ans = [[0]*N for _ in range(N)]

for i in range(N):
    for j, k in enumerate(input().rstrip()):
        if k in '123456789':
            bomb.append((i, j, int(k)))
            ans[i][j] = '*'

for i, j, k in bomb:
    for di, dj in d:
        if 0 <= (ni:=i+di) < N and 0 <= (nj:=j+dj) < N:
            if (t:=ans[ni][nj]) !='*' and t != 'M':
                t += k
                if t >= 10:
                    ans[ni][nj] = 'M'
                else: ans[ni][nj] = t

print("\n".join("".join(map(str, row)) for row in ans))