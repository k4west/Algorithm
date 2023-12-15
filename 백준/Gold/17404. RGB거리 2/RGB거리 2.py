import sys
input = sys.stdin.readline

N = int(input())
inf = float('inf')
rgb = [list(map(int, input().split())) for _ in range(N)]
r = [rgb[0][0], inf, inf]
g = [inf, rgb[0][1], inf]
b = [inf, inf, rgb[0][2]]

for i in range(1, N-1):
    r = min(r[1:]) + rgb[i][0], min(r[0], r[2]) + rgb[i][1], min(r[:2]) + rgb[i][2] 
    g = min(g[1:]) + rgb[i][0], min(g[0], g[2]) + rgb[i][1], min(g[:2]) + rgb[i][2] 
    b = min(b[1:]) + rgb[i][0], min(b[0], b[2]) + rgb[i][1], min(b[:2]) + rgb[i][2] 

print(min(rgb[N-1][0] + min((*g[1:], *b[1:])), rgb[N-1][1] + min((r[0], r[2], b[0], b[2])), rgb[N-1][2] + min((*r[:2], *g[:2]))))
