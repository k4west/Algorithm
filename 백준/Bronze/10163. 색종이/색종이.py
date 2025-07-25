from sys import stdin
input = stdin.readline

plane = [[0]*1001 for _ in range(1001)]
N = int(input())
for i in range(N):
    x, y, w, h = map(int, input().split())
    for r in range(x, x+w):
        for c in range(y, y+h):
            plane[r][c] = i+1

ans = [0 for _ in range(N)]
for i in range(1001):
    for j in range(1001):
        if k := plane[i][j]:
            ans[k-1] += 1
print('\n'.join(map(str, ans)))