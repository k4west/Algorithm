def get_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def get_chic_dist():
    for i in range(H):
        for j in range(C):
            distances[i][j] = get_dist(houses[i], chickens[j])


def bt(n, s, li):
    global min_dist

    if n:
        total = sum(min(distances[i][j] for j in li) for i in range(H))
        if min_dist > total:
            min_dist = total

    if n == M:
        return

    for i in range(s, C):
        bt(n+1, i+1, li+[i])


min_dist = 10000
N, M = map(int, input().split())

houses = []
chickens = []
for r in range(N):
    for c, t in enumerate(input().split()):
        if t == "1":
            houses.append((r, c))
        elif t == "2":
            chickens.append((r, c))

C, H = len(chickens), len(houses)
distances = [[0]*C for _ in range(H)]
get_chic_dist()

bt(0, 0, [])
print(min_dist)