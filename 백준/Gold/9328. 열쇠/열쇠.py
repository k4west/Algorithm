def dfs(h, w):
    if (k := ord(building[h][w])) == 42:
        return 0

    docu = 0
    building[h][w] = "*"
    if k == 36:
        docu += 1
    elif 96 < k < 123:
        keys.add(k)
        if k in locked:
            for i, j in locked.pop(k):
                docu += dfs(i, j)
    elif 64 < k < 91:
        if (kk := k + 32) not in keys:
            if kk not in locked:
                locked[kk] = []
            locked[kk].extend(
                [(nh, nw) for dh, dw in d if check((nh := h + dh), (nw := w + dw))]
            )
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
        keys = set(map(ord, input().rstrip()))

        for i in range(H):
            for j in range(W):
                if i == 0 or i == H - 1 or j == 0 or j == W - 1:
                    documents += dfs(i, j)
        ans.append(str(documents))

    print("\n".join(ans))