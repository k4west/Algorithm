def get_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def f(i, j, safe):
    global ans

    if i > N or (j+N-i) < K:
        return

    if j == K:
        t = max(min(distances[s][k] for s in safe) for k in range(N) if k not in safe)
        if ans > t:
            ans = t
        return

    f(i+1, j, safe)
    f(i+1, j+1, safe+[i])


ans = float("inf")
N, K = map(int, input().split())
houses = [[*map(int, input().split())] for _ in range(N)]

distances = [[0]*N for _ in range(N)]
for r in range(N):
    for c in range(r+1, N):
        dist = get_dist(houses[r], houses[c])
        distances[r][c] = dist
        distances[c][r] = dist

if N == K:
    ans = 0
else:
    f(0, 0, [])
print(ans)
