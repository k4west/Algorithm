def dfs(h, w):
    if (t := building[h][w]) == "*":
        return 0

    docu = 0
    building[h][w] = "*"
    if t == "$":
        docu += 1
    elif 96 < (k := ord(t)) < 123:
        keys.add(t)
        if t in locked:
            for i, j in locked.pop(t):
                docu += dfs(i, j)
    elif 64 < k < 91:
        if (tt := t.lower()) not in keys:
            if tt not in locked:
                locked[tt] = []
            locked[tt].extend([(nh, nw) for dh, dw in d if check((nh := h + dh), (nw := w + dw))])
            return docu

    for dh, dw in d:
        if check((nh := h + dh), (nw := w + dw)):
            docu += dfs(nh, nw)
    return docu


if __name__ == "__main__":
    import sys

    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    ans = []

    for _ in range(int(input())):
        documents, locked = 0, {}
        H, W = map(int, input().split())
        check = lambda x, y: 0 <= x < H and 0 <= y < W
        building = [list(input().rstrip()) for _ in range(H)]
        keys = set(input().rstrip())

        doors = [(i, j) for i in range(H) for j in range(W) if (i == 0 or i == H - 1) or (j == 0 or j == W - 1)]
        while doors:
            h, w = doors.pop()
            documents += dfs(h, w)
        ans.append(str(documents))

    print("\n".join(ans))
