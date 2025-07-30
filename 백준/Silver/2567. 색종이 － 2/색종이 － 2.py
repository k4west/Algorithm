paper = [[0]*100 for _ in range(100)]
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
ans = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

for i in range(100):
    for j in range(100):
        if paper[i][j] == 0:
            for di, dj in d:
                ni, nj = i+di, j+dj
                if 0 <= ni < 100 and 0 <= nj < 100 and paper[ni][nj]:
                    ans += 1
print(ans + sum(paper[0] + paper[99] + [paper[i][0] + paper[i][99] for i in range(100)]))
