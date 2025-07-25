from sys import stdin
input = stdin.readline

area = 1
N, M = map(int, input().split())
rect = [input() for _ in range(N)]
for i in range(N-1):
    for j in range(M-1):
        n = rect[i][j]
        for p in range(i+1, min(N, M + i - j)):
            if rect[p][j] == n == rect[i][j+p-i] == rect[p][j+p-i]:
                if area < (t := (p-i+1)**2):
                    area = t

print(area)
