import sys

input = sys.stdin.readline
ans = []
for _ in range(int(input())):
    n, m = map(int, input().split())
    scores = [[0, 0] for _ in range(n + 1)]
    for _ in range(m):
        a, b, p, q = map(int, input().split())
        scores[a][0] += p
        scores[a][1] += q
        scores[b][0] += q
        scores[b][1] += p
    ws = [score[0] ** 2 / (score[0] ** 2 + score[1] ** 2) if score != [0, 0] else 0 for score in scores[1:]]
    ma, mi = 0, 1
    for w in ws:
        if ma < w:
            ma = w
        if mi > w:
            mi = w
    ans.append(int(1000*ma))
    ans.append(int(1000*mi))
print(*ans, sep='\n')