from itertools import combinations


def check(li):
    global ans

    v = [0]*25
    x, y = li[0]//5, li[0]%5
    q = [(x, y)]
    v[x*5+y] = 1

    while q:
        x, y = q.pop()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            j = nx*5 + ny
            if 0 <= nx < 5 and 0 <= ny < 5 and not v[j] and j in li:
                v[j] = 1
                q.append((nx, ny))

    if sum(v) == 7:
        ans += 1


ans = 0
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
graph = [input() for _ in range(5)]

for candi in combinations(range(25), 7):
    cnt = 0
    for i in candi:
        r, c = i // 5, i % 5
        cnt += (graph[r][c] == "S")
    if cnt >= 4:
        check(candi)

print(ans)