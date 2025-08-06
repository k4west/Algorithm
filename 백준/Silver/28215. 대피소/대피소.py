def get_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def f(i, j, safe):
    global ans

    if i > N or (j+N-i) < K:
        return

    if j == K:
        t = max(min(get_dist(h, houses[s]) for s in safe) for k, h in enumerate(houses) if k not in safe)
        if ans > t:
            ans = t
        return

    f(i+1, j, safe)
    f(i+1, j+1, safe+[i])


ans = float("inf")
N, K = map(int, input().split())
houses = [[*map(int, input().split())] for _ in range(N)]
visited = [0]*N
f(0, 0, [])
print(ans)
