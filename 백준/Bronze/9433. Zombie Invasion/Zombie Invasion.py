for _ in range(int(input())):
    p = [*map(int, input().split())]; r = 0
    for i in range(19, 0, -1): r, p[i] = divmod(p[i] + r, 2)
    p[0] += r; print(*p)