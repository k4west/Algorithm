M, N, H = map(int, input().split())
tomato = [[] for _ in range(H)]
ripen = []
unripe = 0

# 1: 익은 토마토
# 0: 안 익은 토마토
# -1: 토마토 없음
for h in range(H):
    for n in range(N):
        *row, = map(int, input().split())
        tomato[h].append(row)
        for m, t in enumerate(row):
            if t == 0:
                unripe += 1
            elif t == 1:
                ripen.append((h, n, m))
                tomato[h][n][m] = -1

if not unripe:
    print(0)
elif not ripen:
    print(-1)
else:
    days = 0
    d = ((-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (0, -1, 0))  # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
    new_ripen = []

    # 익은 토마토 인접을 탐색
    while ripen or new_ripen:
        if not ripen:
            ripen, new_ripen = new_ripen, []
            days += 1

        h, n, m = ripen.pop()   # 순서 상관 없어서 pop(0) 대신 그냥 pop()
        for dh, dm, dn in d:
            nh = h + dh
            nn = n + dn
            nm = m + dm
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and not tomato[nh][nn][nm]:
                unripe -= 1
                new_ripen.append((nh, nn, nm))
                tomato[nh][nn][nm] = -1

    if unripe:
        print(-1)
    else:
        print(days)
